from fastapi import FastAPI, HTTPException
import services
from schemas import Register
app = FastAPI()

@app.get("/")
def say_hello():
    return {"information": "Hello World!"}


@app.post("/register")
def register_user(user:Register):
    return services.register_user(user)