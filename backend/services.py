import repository
import exceptions
from auth import hash_password, check_hash_password, create_jwt_token, decode_jwt_token
import subprocess
from config import REPOSITORY_PATH


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
    try:
        if repository.check_user_email_exist(user.email) is None:
            raise exceptions.EmailDoesNotExistsError("Whis email does not exists")
        if not valid_email(user.email):
            raise exceptions.InvalidEmailError("This email is invalid")

        password = repository.get_user_password(user.email)
        if not check_hash_password(user.password, password):
            raise exceptions.InvalidPasswordError("Whis password is incorrect")

        response = repository.check_login(user.email)
        if response is None:
            raise exceptions.USerNotFoundError("User with this email doesn't exists")
        else:
            return create_jwt_token(response, user.email)
    except Exception as e :
        raise exceptions.UserLoginError(str(e))

def create_repository(repo, jwt):
    user_info = decode_jwt_token(jwt)
    repository_path = REPOSITORY_PATH /f"{user_info["name"]}/{repo.name}"

    repository.create_repository(repo, user_info["id"])

    subprocess.run(
        ["git", "init", "--bare", str(repository_path)],
        check=True
    )


