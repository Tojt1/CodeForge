from fastapi import FastAPI
from database import engine
from sqlalchemy import text
app = FastAPI()

@app.get("/")
def say_hello():
    return {"information": "Hello World!"}

@app.get("/db-health")
def check_db():
    with engine.connect() as con:
        con.execute(text("SELECT 1"))

    return {"db":"connected"}