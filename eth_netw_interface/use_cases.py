from datetime import datetime, timezone

from contract_manager.repository.repository import DeployedContractRepository
from eth_netw_interface import EthNetworkHTTPInterface
from model import Account, CompiledContract, DeployedContract


def deploy_contract(
    account_from: Account,
    compiled_contact: CompiledContract,
    contract_constructor_kwargs: dict = None,
) -> DeployedContract:
    """
    Deploy a contract on the configured Eth network and store a snapshot of the data
    of the contract.
    ::param:: sol_version solc version to use. e.g. "0.8.17"
    """
    if contract_constructor_kwargs is None:
        contract_constructor_kwargs = {}
    eth_interface = EthNetworkHTTPInterface()
    tx_receipt, tx_hash = eth_interface.deploy_compiled_contract(
        account_from, compiled_contact, contract_constructor_kwargs
    )
    timestamp = datetime.now(timezone.utc)
    deployed_contract = DeployedContract(
        abi=compiled_contact.abi,
        address=tx_receipt.contractAddress,
        bytecode=compiled_contact.bytecode,
        solidity_code=compiled_contact.solidity_code,
        timestamp=timestamp,
    )
    print(f"Contract deployed at address: { tx_receipt.contractAddress }")
    return DeployedContractRepository().persist(deployed_contract)
