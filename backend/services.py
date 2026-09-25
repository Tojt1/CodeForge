import repository
import exceptions
from auth import hash_password
from auth import check_hash_password

def valid_email(email):
    if "@" in email:
        return True

    return False



def register_user(user):
    try:
        if not repository.check_user_email_exist(user.email) is None:
            raise exceptions.EmailAdressInUseError("Whis email is already in use")
        if not valid_email(user.email):
            raise exceptions.InvalidEmailError("This email is invalid")

        hashed_password = hash_password(user.password)

        return repository.register_user(user.name, user.email, user.age, hashed_password)
    except Exception as e:
        raise exceptions.RegisterUserError(str(e))

def sing_in(user):
    if repository.check_user_email_exist(user.email) is None:
        raise exceptions.EmailDoesNotExistsError()
    if not valid_email(user.email):
        raise exceptions.InvalidEmailError()

    password = repository.get_user_password(user.email)
    if not check_hash_password(user.password, password):
        raise exceptions.InvalidPasswordError()

    if not repository.check_login(user.email) is None:
        return {"Information": "Pomyślnie zalogowano"}

