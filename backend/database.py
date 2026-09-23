import sqlalchemy

SQL_ALCHEMY_URL = "postgresql://postgres:postgres@db:5432/codeforge"
engine = sqlalchemy.create_engine(SQL_ALCHEMY_URL)

