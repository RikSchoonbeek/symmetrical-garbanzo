from sqlalchemy import create_engine

from contract_manager.repository import Base


def create_db_schema():
    """
    Apply model to database
    Insightful SO Q&A about using Base and create_all correct: https://stackoverflow.com/questions/54118182/sqlalchemy-not-creating-tables
    More info in docs: https://docs.sqlalchemy.org/en/14/core/metadata.html
    """
    engine = create_engine(f"sqlite:///contract_data.db")
    Base.metadata.create_all(engine)
