from pydantic import BaseModel

class Register(BaseModel):
    user_name: str
    email: str
    password:str
    age: int