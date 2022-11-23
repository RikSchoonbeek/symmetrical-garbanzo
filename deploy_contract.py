from os import getenv
from pathlib import Path

from dotenv import load_dotenv

from contract_helpers import compile_from_contract_sol_file_path
from eth_netw_interface import EthNetworkHTTPInterface
from model import Account


if __name__ == "__main__":
    # Load env vars
    env_file_path = Path().parent / ".env"
    load_dotenv(env_file_path)
    network_chain_id = getenv("GOERLI_CHAIN_ID")
    http_provider_url = getenv("HTTP_PROVIDER_URL")
    wallet_address = getenv("ETH_WALLET_ADDRESS")
    wallet_pk = getenv("ETH_WALLET_PK")

    # Set up interface for Ethereum network
    eth_interface = EthNetworkHTTPInterface(http_provider_url)

    # Compile and deploy contract
    contract_solidity_version = "0.8.17"
    contract_file_name = "UserData.sol"
    path_to_contract_file = Path().parent / "contracts" / contract_file_name
    account_from = Account(wallet_address, wallet_pk)
    contract_compile_data = compile_from_contract_sol_file_path(
        path_to_contract_file, contract_solidity_version
    )
    tx_address = eth_interface.deploy_compiled_contract(
        account_from=account_from, contract_data=contract_compile_data
    )
    print(f"Contract deployed at address: { tx_address }")
