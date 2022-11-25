from datetime import datetime, timezone

from contract_manager.use_cases import (
    get_compiled_contract_data,
    persist_contract_deployment_data,
)
from eth_netw_interface import EthNetworkHTTPInterface
from model import Account


def deploy_contract(
    account_from: Account, contract_name: str, contract_kwargs: dict = {}
):
    """
    Deploy a contract on the configured Eth network and store a snapshot of the data
    of the contract.
    ::param:: sol_version solc version to use. E.g. "0.8.17"
    """
    eth_interface = EthNetworkHTTPInterface()
    compiled_contract_data = get_compiled_contract_data(contract_name)
    tx_receipt, tx_hash = eth_interface.deploy_compiled_contract(
        account_from, compiled_contract_data, contract_kwargs
    )
    timestamp = datetime.now(timezone.utc)
    deployed_contract_data = {
        "abi": compiled_contract_data.abi,
        "address": tx_receipt.contractAddress,
        "bytecode": compiled_contract_data.bytecode,
        "solidity_code": compiled_contract_data.solidity_code,
        "timestamp": timestamp.isoformat(),
    }
    persist_contract_deployment_data(contract_name, deployed_contract_data, timestamp)
    print(f"Contract deployed at address: { tx_receipt.contractAddress }")
