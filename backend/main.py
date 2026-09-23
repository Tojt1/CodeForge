from fastapi import FastAPI, HTTPException
from models import check_user_email_exist
app = FastAPI()

@app.get("/")
def say_hello():
    return {"information": "Hello World!"}


@app.get("/register")
def register_user():
    if check_user_email_exist("w") is None:
        return {"error": "Nie ma użytkownika"}
    else:
        return {"information": "Jest uzytkownik"}