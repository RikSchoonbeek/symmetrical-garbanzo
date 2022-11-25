# TODO I wonder if this is the most logical location for this file, which other
#   packages/modules use this?
from collections import namedtuple

# abstractions of Ethereum network concepts
Account = namedtuple("Account", ["address", "private_key"])
CompiledContract = namedtuple("CompiledContract", ["abi", "bytecode", "solidity_code"])
DeployedContract = namedtuple("DeployedContract", ["address", "abi"])
