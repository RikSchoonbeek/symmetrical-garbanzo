from sqlalchemy import create_engine

from contract_manager.repository import Base


def create_db_schema():
    """
    Apply model to database
    more info in docs: https://docs.sqlalchemy.org/en/14/core/metadata.html
    """
    engine = create_engine(f"sqlite:///contract_data.db")
    Base.metadata.create_all(engine)
