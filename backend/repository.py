from sqlalchemy.orm import Session
from database import engine
import sqlalchemy
from models import Users
import exceptions

def check_user_email_exist(email):
    with Session(engine) as session:
        stmt = sqlalchemy.select(Users).where(Users.email == email)
        return session.execute(stmt).one_or_none()

def register_user(name, email, age):
    try:
        with Session(engine) as session:
            user = Users(user_name=name,
                         email=email,
                         age=age)

            session.add(user)
            session.commit()
    except Exception as e:
        raise exceptions.AddusertoDBError(str(e))