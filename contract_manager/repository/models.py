from __future__ import annotations
import json

from sqlalchemy import Column, DateTime, Integer, String, Text

from model import CompiledContract, DeployedContract
from contract_manager.repository import Base


class CompiledContractDB(Base):
    __tablename__ = "compiled_contract"

    pk = Column(Integer, primary_key=True)
    abi = Column(Text)
    # TODO I wonder how bytecode is best stored
    bytecode = Column(Text)
    name = Column(String(128))
    solidity_code = Column(Text)
    timestamp = Column(DateTime)

    def __repr__(self):
        return f"CompiledContractDB(name={self.name}, ts={self.timestamp.isoformat()})"

    @classmethod
    def from_domain_instance(cls, instance: CompiledContract) -> CompiledContractDB:
        return cls(
            abi=json.dumps(instance.abi),
            bytecode=instance.bytecode,
            name=instance.name,
            solidity_code=instance.solidity_code,
            timestamp=instance.timestamp,
        )

    def to_domain_instance(self) -> CompiledContract:
        return CompiledContract(
            abi=json.loads(self.abi),
            bytecode=self.bytecode,
            name=self.name,
            solidity_code=self.solidity_code,
            timestamp=self.timestamp,
        )


class DeployedContractDB(Base):
    __tablename__ = "deployed_contract"

    abi = Column(Text)
    # TODO store 32 bytes hex as string ? There may be a more optimal solution
    address = Column(String(34), primary_key=True)
    # TODO I wonder how bytecode is best stored
    bytecode = Column(Text)
    solidity_code = Column(Text)
    timestamp = Column(DateTime)

    def __repr__(self):
        return f"DeployedContractDB(addr={self.address[:20]}, ts={self.timestamp.isoformat()})"

    @classmethod
    def from_domain_instance(cls, instance: DeployedContract) -> DeployedContractDB:
        return cls(
            abi=instance.abi,
            address=instance.address,
            bytecode=instance.bytecode,
            solidity_code=instance.solidity_code,
            timestamp=instance.timestamp,
        )

    def to_domain_instance(self) -> DeployedContract:
        return DeployedContract(
            abi=self.abi,
            address=self.address,
            bytecode=self.bytecode,
            solidity_code=self.solidity_code,
            timestamp=self.timestamp,
        )
