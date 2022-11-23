from os import getenv
from pathlib import Path

from dotenv import load_dotenv

from main_use_cases import deploy_contract
from model import Account


env_file_path = Path().parent / ".env"
load_dotenv(env_file_path)


def test_deploy_contract():
    wallet_address = getenv("ETH_WALLET_ADDRESS")
    wallet_pk = getenv("ETH_WALLET_PK")
    account_from = Account(wallet_address, wallet_pk)
    contract_name = "UserData"
    deploy_contract(account_from, contract_name)

    # TODO probably assert that the deployment worked
    #   and we may want to use a test version of web3.py for this


# TODO This is a temporary way to interact with the use cases
if __name__ == "__main__":
    test_deploy_contract()
