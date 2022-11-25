"""
This file acts as a temporary way to call the use cases in the contract_manager
This will probably be replaced with tests at some point, but I will need to find
out how to work with a mocked network with web3.py. But the idea is kind of similar
and function as a showcase for how the contract_manager can be used.
"""
from contract_manager.use_cases import compile_contract

# TODO add call for compiling each of the added contracts using
# contract_manager.use_cases.compile_contract
def call_compile_contract():
    # contract_name = "UserData"
    contract_name = "PrimitiveWhitelist"
    contract_solidity_version = "0.8.17"
    compile_contract(contract_name, contract_solidity_version)


if __name__ == "__main__":
    # Here I can call the functions in this file, and comment out the ones I don't want to be executed.
    call_compile_contract()
