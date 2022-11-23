from compile import compile_contract


def compile_all_contracts():
    contract_name = "UserData"
    contract_solidity_version = "0.8.17"
    compile_contract(contract_name, contract_solidity_version)


if __name__ == "__main__":
    compile_all_contracts()
