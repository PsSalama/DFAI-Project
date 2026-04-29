from pydantic import BaseModel

class register_data(BaseModel):
    full_name: str|None = "test"
    email: str
    password: str