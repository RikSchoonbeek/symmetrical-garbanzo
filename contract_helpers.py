from pathlib import Path
from typing import Optional

import solcx
from web3 import Web3

from model import Account, ContractCompileData


def compile_from_contract_sol_file_path(
    file_path: Path,
    sol_version: Optional[str] = None,
) -> ContractCompileData:
    """
    Pass a path to a .sol file, optionally pass a the version of the solidity compiler to use (matching the solidity version of the .sol file)
    ::param:: sol_version solc version to use. May be given as a string or Version object. If not given, the
              currently active version is used. Ignored if solc_binary is also given.
              https://solcx.readthedocs.io/en/latest/using-the-compiler.html?highlight=compile_standard#compiling-with-the-standard-json-format
    """
    # TODO make this optional: only install if version isn't installed yet?
    # Download and install a precompiled solc binary
    # https://solcx.readthedocs.io/en/latest/version-management.html?highlight=install_solc#installing-precompiled-binaries
    solcx.install_solc(sol_version)

    with file_path.open() as contract_file:
        contract_file_content = contract_file.read()

    compiled_solidity = solcx.compile_standard(
        {
            "language": "Solidity",
            "sources": {
                "UserData.sol": {
                    "content": contract_file_content,
                }
            },
            "settings": {
                "outputSelection": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version=sol_version,
    )

    file_name_with_ext = file_path.name
    file_name_no_ext = file_path.stem
    contract_data = compiled_solidity["contracts"][file_name_with_ext][file_name_no_ext]
    return ContractCompileData(
        contract_data["abi"], contract_data["evm"]["bytecode"]["object"]
    )


# TODO it doesn't seem right that w3 should be passed like this, does this hint to a more clean
#   way of putting things together? Maybe an interface around the Web3 object, i.e. exposing the things
#   that I want to be able to do?
def deploy_compiled_contract(
    w3: Web3, account_from: Account, contract_data: ContractCompileData
) -> str:
    contract_before_deploy = w3.eth.contract(
        abi=contract_data.abi, bytecode=contract_data.bytecode
    )
    contract_constructor = contract_before_deploy.constructor()
    built_tx = contract_constructor.build_transaction(
        {
            "from": account_from.address,
            "nonce": w3.eth.get_transaction_count(account_from.address),
        }
    )
    signed_tx = w3.eth.account.sign_transaction(built_tx, account_from.private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt.contractAddress
