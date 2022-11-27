"""
Use cases for interacting with contract files:
- initiating solidity file compilation
- retrieval of compiled contract's data as model.CompiledContract, from contract's .json file
"""
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Optional

import solcx

from contract_manager.repository.repository import (
    CompiledContractRepository,
)
from model import CompiledContract
import settings


def compile_contract(
    contract_name: str,
    sol_version: Optional[str] = None,
) -> CompiledContract:
    """
    Compile contract solidity file bytecode, while also generating the abi, persist in repo
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

    timestamp = datetime.now(timezone.utc)
    compilation_result = solcx.compile_standard(
        {
            "language": "Solidity",
            "sources": {
                f"{contract_name}.sol": {
                    "content": contract_file_content,
                }
            },
            "settings": {
                "outputSelection": {
                    # Currently not doing anything with metadata or evm.sourceMap, but
                    # might be valuable to store
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        allow_paths=settings.PY_SOLCX_ALLOWED_PATHS,
        solc_version=sol_version,
    )

    contract_data = compilation_result["contracts"][f"{contract_name}.sol"][
        contract_name
    ]
    compiled_contract = CompiledContract(
        abi=contract_data["abi"],
        bytecode=contract_data["evm"]["bytecode"]["object"],
        name=contract_name,
        solidity_code=contract_file_content,
        timestamp=timestamp,
    )
    return CompiledContractRepository().persist(compiled_contract)


def get_compiled_contract_data(contract_name: str) -> CompiledContract:
    file_path = Path(f"contract_manager/compiled/{contract_name}.json")
    with open(file_path, "r", encoding="utf-8") as file:
        compiled_data = json.load(file)
    return CompiledContract(
        compiled_data["abi"], compiled_data["bytecode"], compiled_data["solidity_code"]
    )
