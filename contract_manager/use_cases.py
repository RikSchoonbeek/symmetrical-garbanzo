"""
Use cases for interacting with contract files:
- initiating solidity file compilation
- retrieval of compiled contract's data as model.CompiledContract, from contract's .json file
"""
import json
from pathlib import Path
from typing import Optional

import solcx

from model import CompiledContract


def compile_contract(
    contract_name: str,
    sol_version: Optional[str] = None,
):
    """
    Compile contract solidity file into abi and bytecode
    ::contract_name:: name of contract's .sol file, without extension
    ::param:: sol_version solc version to use, e.g. "0.8.17". If not given, the currently active version is used. Ignored if solc_binary is also given.
              https://solcx.readthedocs.io/en/latest/using-the-compiler.html?highlight=compile_standard#compiling-with-the-standard-json-format
    """
    # TODO make this optional: only install if version isn't installed yet?
    # Download and install a precompiled solc binary
    # https://solcx.readthedocs.io/en/latest/version-management.html?highlight=install_solc#installing-precompiled-binaries
    solcx.install_solc(sol_version)

    contract_file_path = Path(f"contract_manager/solidity_files/{contract_name}.sol")
    with contract_file_path.open("r") as contract_file:
        contract_file_content = contract_file.read()

    compiler_result = solcx.compile_standard(
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

    contract_data = compiler_result["contracts"][f"{contract_name}.sol"][contract_name]
    result_file_path = Path(f"contract_manager/compiled_contracts/{contract_name}.json")
    # TODO ask if file overwrite is ok if already exists?
    with open(result_file_path, "w", encoding="utf-8") as result_file:
        json.dump(
            {
                "abi": contract_data["abi"],
                "bytecode": contract_data["evm"]["bytecode"]["object"],
            },
            result_file,
            sort_keys=True,
            indent=2,
        )


def get_compiled_contract_data(contract_name: str) -> CompiledContract:
    file_path = Path(f"contract_manager/compiled_contracts/{contract_name}.json")
    with open(file_path, "r", encoding="utf-8") as file:
        compiled_data = json.load(file)
    return CompiledContract(compiled_data["abi"], compiled_data["bytecode"])
