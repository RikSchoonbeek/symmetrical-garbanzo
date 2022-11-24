from contract_manager.use_cases import get_compiled_contract_data
from eth_netw_interface import EthNetworkHTTPInterface
from model import Account


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
    # TODO probably also store together:
    #   contract address
    #   abi and bytecode (already available from json file)
    #   snapshot of solidity code of deployed contract
    print(f"Contract deployed at address: { tx_address }")
