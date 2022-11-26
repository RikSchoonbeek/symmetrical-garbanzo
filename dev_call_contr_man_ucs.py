"""
This file acts as a temporary way to call the use cases in the contract_manager
This will probably be replaced with tests at some point, but I will need to find
out how to work with a mocked network with web3.py. But the idea is kind of similar
and function as a showcase for how the contract_manager can be used.
"""
from datetime import datetime

from contract_manager.repository.helpers import create_db_schema
from contract_manager.repository.models import DeployedContractDB
from contract_manager.repository.repository import (
    CompiledContractRepository,
    DeployedContractRepository,
)
from contract_manager.use_cases import compile_contract
from model import DeployedContract


# TODO add call for compiling each of the added contracts using
# contract_manager.use_cases.compile_contract
def call_compile_contract():
    # contract_name = "UserData"
    contract_name = "PrimitiveWhitelist"
    contract_solidity_version = "0.8.17"
    compile_contract(contract_name, contract_solidity_version)
    print()


def test_repo_call():
    # test_instance = DeployedContract(
    #     abi="[{},{}]",
    #     address="0x12345678901234567890123456789012",
    #     bytecode="0x123456789012345678901234567890123456789012345678901234567890",
    #     solidity_code="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    #     timestamp=datetime.now(),
    # )
    # db_instance = DeployedContractDB.from_domain_instance(test_instance)
    # repo = DeployedContractRepository()
    # repo.persist(db_instance)
    contract_name = "PrimitiveWhitelist"
    repo = CompiledContractRepository()
    compiled_contract = repo.filter(name=contract_name)[-1]
    print()


if __name__ == "__main__":
    # Here I can call the functions in this file, and comment out the ones I don't want to be executed.
    create_db_schema()
    call_compile_contract()
    test_repo_call()
    print()
