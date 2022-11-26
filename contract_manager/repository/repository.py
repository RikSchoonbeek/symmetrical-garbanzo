from datetime import datetime
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from contract_manager.repository.models import CompiledContractDB, DeployedContractDB
from model import CompiledContract, DeployedContract

__all__ = (
    "CompiledContractRepository",
    "DeployedContractRepository",
    "Repository",
)


class Repository:
    def __init__(self):
        engine = create_engine(f"sqlite:///contract_data.db")
        Session = sessionmaker()
        Session.configure(bind=engine)
        self._db_session = Session()


class CompiledContractRepository(Repository):
    def filter(self, name: str = None) -> List[CompiledContract]:
        db_instances = self._db_session.query(CompiledContractDB).filter(
            CompiledContractDB.name == name
        )
        return [i.to_domain_instance() for i in db_instances]

    def get(self, name: str = None, timestamp: datetime = None) -> CompiledContract:
        db_instance = (
            self._db_session.query(CompiledContractDB)
            .filter(
                CompiledContractDB.name == name
                and CompiledContractDB.timestamp == timestamp
            )
            .one()
        )
        return db_instance.to_domain_instance()

    def persist(self, contract: CompiledContract):
        db_instance = CompiledContractDB.from_domain_instance(contract)
        self._db_session.add(db_instance)
        self._db_session.commit()


class DeployedContractRepository(Repository):
    def get_by_address(self, address) -> DeployedContract:
        db_instance = self._db_session.query(DeployedContractDB).get(address)
        return db_instance.to_domain_instance()

    def persist(self, contract: DeployedContract):
        db_instance = DeployedContractDB.from_domain_instance(contract)
        self._db_session.add(db_instance)
        self._db_session.commit()
