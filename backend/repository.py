from sqlalchemy.orm import Session
from database import engine
import sqlalchemy
from models import Users
import exceptions


def check_user_email_exist(email):
    with Session(engine) as session:
        stmt = sqlalchemy.select(Users).where(Users.email == email)
        return session.execute(stmt).one_or_none()

def register_user(name, email, age, password):
    try:
        with Session(engine) as session:
            user = Users(user_name=name,
                         email=email,
                         age=age,
                         password=password)

            session.add(user)
            session.commit()
    except Exception as e:
        raise exceptions.AddusertoDBError(str(e))

def get_user_password(email):
    with Session(engine) as session:
        query = sqlalchemy.select(Users.password).where(Users.email == email)
        return session.execute(query).scalar_one_or_none()

def check_login(email):
    with Session(engine) as session:
        query = sqlalchemy.select(Users.id).where(Users.email == email)
        return session.execute(query).scalar_one_or_none()
