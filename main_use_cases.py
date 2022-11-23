import json
from pathlib import Path

from eth_netw_interface import EthNetworkHTTPInterface
from model import Account, CompiledContract


def deploy_contract(
    account_from: Account,
    contract_name: str,
):
    """
    ::param:: sol_version solc version to use. E.g. "0.8.17"
    """
    eth_interface = EthNetworkHTTPInterface()
    compiled_contract_data = get_compiled_contract_data(contract_name)
    tx_address = eth_interface.deploy_compiled_contract(
        account_from, compiled_contract_data
    )
    print(f"Contract deployed at address: { tx_address }")


# TODO is this more logical as a helper? It doesn't seem like a main use case, more something called by a main use case
def get_compiled_contract_data(contract_name: str) -> CompiledContract:
    file_path = Path(f"contracts/compiled/{contract_name}.json")
    with open(file_path, "r", encoding="utf-8") as file:
        compiled_data = json.load(file)
    return CompiledContract(compiled_data["abi"], compiled_data["bytecode"])
