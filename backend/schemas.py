from pydantic import BaseModel

class Register(BaseModel):
    name: str
    email: str
    password:str
    age: int

class Login(BaseModel):
    email:str
    password:str

class CreateRepository(BaseModel):
    name: str
    description: str