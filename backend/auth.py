import bcrypt

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8") ,bcrypt.gensalt())
    return hashed_password


def unhash_password(password, hash_password):
    return bcrypt.checkpw(password.encode("utf-8"), hash_password)
