# TODO I wonder if this is the most logical location for this file, which other
#   packages/modules use this?
from datetime import datetime
from typing import NamedTuple, Optional

# abstractions of Ethereum network concepts
class Account(NamedTuple):
    address: str
    private_key: str


class CompiledContract(NamedTuple):
    abi: dict
    bytecode: str
    # Name of contract class, and I want to keep the convention of giving the file the same name,
    # but I am not enforcing this. May need better solution in future.
    name: str
    solidity_code: str
    timestamp: datetime
    pk: Optional[int] = None


class DeployedContract(NamedTuple):
    abi: dict
    address: str
    bytecode: str
    solidity_code: str
    timestamp: datetime
