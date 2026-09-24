import repository
import exceptions

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

        return repository.register_user(user.name, user.email, user.age)
    except Exception as e:
        raise exceptions.RegisterUserError(str(e))