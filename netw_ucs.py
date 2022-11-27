"""
This module is meant for implementing different use cases for specific compiled and
deployed contracts.
"""
from os import getenv
from pathlib import Path

from dotenv import load_dotenv

from contract_manager.repository.repository import (
    CompiledContractRepository,
    DeployedContractRepository,
)
from contract_manager.use_cases import compile_contract
from contract_manager.repository.helpers import create_db_schema
from eth_netw_interface import EthNetworkHTTPInterface
from eth_netw_interface.use_cases import deploy_contract
from model import Account
import settings


load_dotenv(settings.DOTENV_FILE_PATH)
account_1 = Account(getenv("ETH_ACCOUNT_ADDRESS_1"), getenv("ETH_ACCOUNT_PK_1"))
account_2 = Account(getenv("ETH_ACCOUNT_ADDRESS_2"), getenv("ETH_ACCOUNT_PK_2"))
account_3 = Account(getenv("ETH_ACCOUNT_ADDRESS_3"), getenv("ETH_ACCOUNT_PK_3"))


def white_list_contract():
    create_db_schema()
    # compile contract and store it's id
    # contract_name = "PrimitiveWhitelist"
    # contract_solidity_version = "0.8.17"
    # compiled_contract = compile_contract(contract_name, contract_solidity_version)
    # print(f"Compiled contract pk: {compiled_contract.pk}")
    # compiled_contract_pk = 1
    # compiled_contract = CompiledContractRepository().get_by_pk(compiled_contract_pk)
    # deployed_contract = deploy_contract(
    #     account_1,
    #     compiled_contract,
    #     contract_constructor_kwargs={"_maxWhitelistedAddresses": 10},
    # )

    chain_id = int(getenv("GOERLI_CHAIN_ID"))
    eth_itf = EthNetworkHTTPInterface()
    deployed_contract_address = "0xcd9b7aC473caC648d6500b5597a9192Ccd5EEf0e"
    deployed_contract = DeployedContractRepository().get_by_address(
        deployed_contract_address
    )
    contract_interface = eth_itf.get_deployed_contract(deployed_contract)
    print(f"Deployed contract address: {deployed_contract.address}")
    # Add account_1 address to the whitelist
    # tx_1_receipt, tx_1_hash = eth_itf.build_sign_send_tx_and_get_receipt(
    #     tx_data={
    #         "gasPrice": eth_itf.w3.eth.gas_price,
    #         "chainId": chain_id,
    #         "from": account_1.address,
    #         "nonce": eth_itf.w3.eth.get_transaction_count(account_1.address),
    #     },
    #     function=contract_interface.functions.addWhitelistAddress(),
    #     sender_private_key=account_1.private_key,
    # )
    # last tx hash: 0x9fbaed8e99bb2c074422b0d989d5364886ac5e585d4d971631ae0a5122938e4d
    print(
        f"Count adresses whitelisted: {contract_interface.functions.numAdressesWhitelisted().call()}"
    )


def custom_nft_presale_mint():
    # compile contract and store it's id
    chain_id = int(getenv("GOERLI_CHAIN_ID"))
    # contract_name = "CustomNFT"
    # contract_solidity_version = "0.8.17"
    # compiled_contract = compile_contract(contract_name, contract_solidity_version)
    # print(f"Compiled contract pk: {compiled_contract.pk}")
    # compiled_contract_pk = 2
    # compiled_contract = CompiledContractRepository().get_by_pk(compiled_contract_pk)
    # deployed_contract = deploy_contract(
    #     account_1,
    #     compiled_contract,
    #     contract_constructor_kwargs={
    #         "baseURI": "https://www.example.com/customnft/",
    #         "whitelistContract": "0xcd9b7aC473caC648d6500b5597a9192Ccd5EEf0e",
    #     },
    # )
    # print(f"Deployed contract address: {deployed_contract.address}")
    eth_itf = EthNetworkHTTPInterface()
    deployed_contract_address = "0xA944620Df83Da42Edf4dD215a479fFA0Cc6d3A0D"
    deployed_contract = DeployedContractRepository().get_by_address(
        deployed_contract_address
    )
    contract_interface = eth_itf.get_deployed_contract(deployed_contract)
    # Start presale

    # # Perform presale mint with whitelisted account_1
    # tx_1_receipt, tx_1_hash = eth_itf.build_sign_send_tx_and_get_receipt(
    #     tx_data={
    #         "gasPrice": eth_itf.w3.eth.gas_price,
    #         "chainId": chain_id,
    #         "from": account_1.address,
    #         "nonce": eth_itf.w3.eth.get_transaction_count(account_1.address),
    #     },
    #     function=contract_interface.functions.startPresale(),
    #     sender_private_key=account_1.private_key,
    # )
    # print(f"Start presale transaction hash: {repr(tx_1_hash)}")
    # # last tx hash: b'\x0f"\xf0\x10\xb6n\xb5t\xf51i\x03\x17h\xd3N<2\x0b\xcd\xac\xd6\x98\xa5:V\xbc\xd7\xd1B\xca\xb4'

    # # Try presale mint with non whitelisted account account_3. This should fail
    # tx_2_receipt, tx_2_hash = eth_itf.build_sign_send_tx_and_get_receipt(
    #     tx_data={
    #         "gasPrice": eth_itf.w3.eth.gas_price,
    #         "chainId": chain_id,
    #         "from": account_3.address,
    #         "nonce": eth_itf.w3.eth.get_transaction_count(account_3.address),
    #     },
    #     function=contract_interface.functions.presaleMint(),
    #     sender_private_key=account_3.private_key,
    # )


if __name__ == "__main__":
    # white_list_contract()
    custom_nft_presale_mint()
