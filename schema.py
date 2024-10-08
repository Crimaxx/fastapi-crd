from pydantic import BaseModel

class Usercreateshcema(BaseModel):
    username:str
    password:str
    class Config:
        extra="forbid"

class Userdeleteschema(BaseModel):
    username:str
    class Config:
        extra="forbid"

class Userupdateshcema(BaseModel):
    new_username:str
    password:str
    class Config:
        extra="forbid"