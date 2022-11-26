from __future__ import annotations

from sqlalchemy import Column, DateTime, String, Text

from model import DeployedContract
from contract_manager.repository import Base


class DeployedContractDB(Base):
    __tablename__ = "deployed_contract"

    abi = Column(Text)
    # TODO store 32 bytes hex as string ? There may be a more optimal solution
    address = Column(String(34), primary_key=True)
    # TODO I wonder how bytecode is best stored
    bytecode = Column(Text)
    solidity_code = Column(Text)
    # TODO make/rename this to datetime? (the domain model in Python should be a datetime object)
    timestamp = Column(DateTime)

    def __repr__(self):
        return f"DeployedContractDB(addr={self.address[:20]}, ts={self.timestamp})"

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
