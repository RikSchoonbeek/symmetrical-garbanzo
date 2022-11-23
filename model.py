from collections import namedtuple

# abstractions of Ethereum network concepts
Account = namedtuple("Account", ["address", "private_key"])
ContractCompileData = namedtuple("ContractCompileData", ["abi", "bytecode"])
