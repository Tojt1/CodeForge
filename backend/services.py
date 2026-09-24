import repository

def valid_email(email):
    if "@" in email:
        return True

    return False



def register_user(user):
    if not repository.check_user_email_exist(user.email) is None:
        return {"information": "Jest uzytkownik"}
    if not valid_email(user.email):
        return {"error":"2"}

    return repository.register_user(user.name, user.email, user.age)