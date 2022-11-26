from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from contract_manager.repository.models import DeployedContractDB
from model import DeployedContract

__all__ = (
    "DeployedContractRepository",
    "Repository",
)


class Repository:
    def __init__(self):
        engine = create_engine(f"sqlite:///contract_data.db")
        Session = sessionmaker()
        Session.configure(bind=engine)
        self._db_session = Session()


class DeployedContractRepository(Repository):
    def get_by_address(self, address) -> DeployedContract:
        db_instance = self._db_session.query(DeployedContractDB).get(address)
        return db_instance.to_domain_instance()

    def persist(self, contract: DeployedContract):
        db_instance = DeployedContractDB.from_domain_instance(contract)
        self._db_session.add(db_instance)
        self._db_session.commit()
