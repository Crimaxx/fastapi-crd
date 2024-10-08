from fastapi import FastAPI,Depends
from db import get_db
from sqlalchemy.orm import Session
from schema import *
from service import *
app = FastAPI()


@app.get("/")
def healthy_check():
    return {"msg":"this is my site"}

@app.get("/user")
def get_user(username: str,db:Session=Depends(get_db)):
    data=get_user_in_db(username=username,db=db)
    return data

@app.post("/user")
def create_user(item: Usercreateshcema,db:Session=Depends(get_db)):
    message=create_user_in_db(data=item,db=db)
    return message

@app.delete("/user")
def delete_user(item:Userdeleteschema,db:Session=Depends(get_db)):
    message=delete_user_in_db(data=item,db=db)
    return message

@app.put("/username")
def update_user_username(username:str,item:Userupdateshcema,db:Session= Depends(get_db)):
    message=update_user_username(current_username=username,data=item,db=db)
    return message
