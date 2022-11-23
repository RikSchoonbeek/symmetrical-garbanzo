from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy

from model import Account, CompiledContract

__all__ = ("EthNetworkHTTPInterface",)


# TODO in the future I may want to have different types of providers, and use inheritance
#   to share common funcationality between the different types of providers
class EthNetworkHTTPInterface:
    """
    TODO
    Interface for use cases for Ethereum network
    """

    def __init__(self, http_provider_url: str) -> None:
        """
        Instantiate instance of web3.Web3, which is the main interface the web3.py package offers
        for interacting with the Ethereum network.
        """
        self._w3 = Web3(Web3.HTTPProvider(http_provider_url))
        # TODO find out what this is, and determine more logical way to do this. I can
        #   imagine a default gas price strat can be set, or determined per transaction?
        #   But having this fixed here isn't what we want probably.
        self._w3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

    def deploy_compiled_contract(
        self, account_from: Account, contract_data: CompiledContract
    ) -> str:
        contract_before_deploy = self._w3.eth.contract(
            abi=contract_data.abi, bytecode=contract_data.bytecode
        )
        contract_constructor = contract_before_deploy.constructor()
        built_tx = contract_constructor.build_transaction(
            {
                "from": account_from.address,
                "nonce": self._w3.eth.get_transaction_count(account_from.address),
            }
        )
        signed_tx = self._w3.eth.account.sign_transaction(
            built_tx, account_from.private_key
        )
        tx_hash = self._w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = self._w3.eth.wait_for_transaction_receipt(tx_hash)
        return tx_receipt.contractAddress
