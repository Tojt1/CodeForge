import bcrypt
import jwt
import config

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8") ,bcrypt.gensalt())
    return hashed_password


def unhash_password(password, hash_password):
    return bcrypt.checkpw(password.encode("utf-8"), hash_password)

def create_jwt_token():
    return jwt.encode({"ala":"kota"}, config.jwt_secret, config.jwt_algorithm)

def decode_jwt_token(encoded_jwt):
    return jwt.decode(encoded_jwt, config.jwt_secret, config.jwt_algorithm)
