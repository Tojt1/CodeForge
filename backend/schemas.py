from pydantic import BaseModel

class Register(BaseModel):
    user_name: str
    email: str
    age: int