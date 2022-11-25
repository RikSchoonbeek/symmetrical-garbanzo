from enum import Enum
from os import getenv
from pathlib import Path
import random
from typing import NamedTuple

from dotenv import load_dotenv

from contract_manager.use_cases import get_compiled_contract_data
from eth_netw_interface import EthNetworkHTTPInterface
from eth_netw_interface.use_cases import deploy_contract
from model import Account, DeployedContract


env_file_path = Path().parent / ".env"
load_dotenv(env_file_path)


def test_deploy_contract():
    wallet_address = getenv("ETH_WALLET_ADDRESS")
    wallet_pk = getenv("ETH_WALLET_PK")
    account_from = Account(wallet_address, wallet_pk)
    contract_name = "PrimitiveWhitelist"
    contract_kwargs = {"_maxWhitelistedAddresses": 10}
    deploy_contract(account_from, contract_name, contract_kwargs)

    # TODO probably assert that the deployment worked
    #   and we may want to use a test version of web3.py for this


def test_interact_with_user_data_contract():
    # get api with contract
    eth_itf = EthNetworkHTTPInterface()

    contract_name = "UserData"
    contract_data = get_compiled_contract_data(contract_name)
    contract_address = "0x0FdDb53BCCAD2f5D17A1686BaAE625C0B61F7074"
    deployed_contract = DeployedContract(contract_address, contract_data.abi)
    contract = eth_itf.get_deployed_contract(deployed_contract)

    chain_id = int(getenv("GOERLI_CHAIN_ID"))
    wallet_address = getenv("ETH_WALLET_ADDRESS")
    wallet_pk = getenv("ETH_WALLET_PK")
    account_from = Account(wallet_address, wallet_pk)

    # Creating these abstractions (User and Gender), WITH VALIDATION
    # could be useful for guaranteeing correctness of input and understanding
    # of output of interacting with contracts
    # TODO I would probably need to explore a logical way of storing such abstractions.
    class Gender(Enum):
        female = "F"
        male = "M"

    # TODO this seems to be the currently preferred way over namedtuple. Replace others
    class User(NamedTuple):
        name: str  # TODO set and validate max length
        gender: Gender

    # This is free as the blockchain state isn't changed, therefore a transaction is not required
    u_name, u_gender = contract.functions.getUser().call()
    returned_user = User(u_name, u_gender)
    print(f"Returned user name: {returned_user.name} gender: {returned_user.gender}")

    name_choices = ["Baam", "Rikkert"]
    gender_choices = [Gender.female, Gender.male]
    user_to_set = User(random.choice(name_choices), random.choice(gender_choices))
    # This costs gas, as the blockhain state is changed Therefore a transaction is required.
    tx_receipt, tx_hash = eth_itf.build_sign_send_tx_and_get_receipt(
        tx_data={
            "gasPrice": eth_itf.w3.eth.gas_price,
            "chainId": chain_id,
            "from": account_from.address,
            "nonce": eth_itf.w3.eth.get_transaction_count(account_from.address),
        },
        function=contract.functions.setUser(user_to_set.name, user_to_set.gender.value),
        sender_private_key=account_from.private_key,
    )
    print(
        f"Set user name: {user_to_set.name} gender: {user_to_set.gender} in transaction with hash {tx_hash.hex()}"
    )

    # This is free as the blockchain state isn't changed
    u_name, u_gender = contract.functions.getUser().call()
    returned_user = User(u_name, u_gender)
    print(f"Returned user name: {returned_user.name} gender: {returned_user.gender}")


# TODO This is a temporary way to interact with the use cases
if __name__ == "__main__":
    test_deploy_contract()
    # test_interact_with_user_data_contract()
