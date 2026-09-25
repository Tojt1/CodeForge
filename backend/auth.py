import bcrypt
import jwt
import config

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8") ,bcrypt.gensalt()).decode("utf-8")
    return hashed_password


def check_hash_password(password, hash_password):
    return bcrypt.checkpw(password.encode("utf-8"), hash_password.encode("utf-8"))

def create_jwt_token(user_inf, email):
    return jwt.encode({
        "id":user_inf["id"],
        "name":user_inf["user_name"],
        "age":user_inf["age"],
        "email":email
    }, config.jwt_secret, config.jwt_algorithm)

def decode_jwt_token(encoded_jwt):
    return jwt.decode(encoded_jwt, config.jwt_secret, config.jwt_algorithm)
