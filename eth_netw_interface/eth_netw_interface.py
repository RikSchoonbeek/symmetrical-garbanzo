from os import getenv
from pathlib import Path
from typing import Tuple

from dotenv import load_dotenv
from hexbytes.main import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.gas_strategies.rpc import rpc_gas_price_strategy

from model import Account, CompiledContract, DeployedContract

__all__ = ("EthNetworkHTTPInterface",)


# TODO in the future I may want to have different types of providers, and use inheritance
#   to share common funcationality between the different types of providers
class EthNetworkHTTPInterface:
    """
    TODO
    Interface for use cases for Ethereum network
    """

    def __init__(self) -> None:
        """
        Instantiate instance of web3.Web3, which is the main interface the web3.py package offers
        for interacting with the Ethereum network.
        """
        env_file_path = Path().parent / ".env"
        load_dotenv(env_file_path)
        http_provider_url = getenv("HTTP_PROVIDER_URL")
        self.w3 = Web3(Web3.HTTPProvider(http_provider_url))
        # TODO find out what this is, and determine more logical way to do this. I can
        #   imagine a default gas price strat can be set, or determined per transaction?
        #   But having this fixed here isn't what we want probably.
        self.w3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

    def deploy_compiled_contract(
        self,
        account_from: Account,
        contract_data: CompiledContract,
        contract_kwargs: dict = {},
    ) -> str:
        contract_before_deploy = self.w3.eth.contract(
            abi=contract_data.abi, bytecode=contract_data.bytecode
        )
        contract_constructor = contract_before_deploy.constructor(**contract_kwargs)
        transaction_data = {
            "from": account_from.address,
            "nonce": self.w3.eth.get_transaction_count(account_from.address),
        }
        tx_receipt, tx_hash = self.build_sign_send_tx_and_get_receipt(
            function=contract_constructor,
            tx_data=transaction_data,
            sender_private_key=account_from.private_key,
        )
        return tx_receipt, tx_hash

    def build_sign_send_tx_and_get_receipt(
        self, function: ContractFunction, tx_data: dict, sender_private_key: str
    ) -> Tuple[AttributeDict, HexBytes]:
        built_tx = function.build_transaction(tx_data)
        signed_tx = self.w3.eth.account.sign_transaction(built_tx, sender_private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # TODO This could raise an TimeExhausted (see method details). This should probably be handled.
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return (tx_receipt, tx_hash)

    def get_deployed_contract(self, deployed_contract: DeployedContract):  # -> TODO
        return self.w3.eth.contract(
            address=deployed_contract.address, abi=deployed_contract.abi
        )
