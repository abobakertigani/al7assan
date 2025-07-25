# schemas/auth.py
from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str
    password: str
