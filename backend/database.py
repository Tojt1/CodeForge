import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

SQL_ALCHEMY_URL = "postgresql://postgres:postgres@db:5432/codeforge"
engine = sqlalchemy.create_engine(SQL_ALCHEMY_URL)

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(sqlalchemy.String(50))
    email: Mapped[str] = mapped_column(sqlalchemy.String(255), unique=True)
    age: Mapped[int] = mapped_column(sqlalchemy.Integer)
    is_active: Mapped[bool] = mapped_column(default=True)
    created: Mapped[datetime.datetime] = mapped_column(sqlalchemy.DateTime, server_default=sqlalchemy.func.now())


