from models import User
from schema import *
from sqlalchemy.orm import Session
from fastapi import HTTPException
def create_user_in_db(data:Usercreateshcema,db:Session):
    new_user=User(username=data.username,password=data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"new user is created"}

def delete_user_in_db(data:Userdeleteschema,db:Session):
    user_in_db= db.query(User).filter(User.username==data.username).first()
    db.delete(user_in_db)
    db.commit()
    return {"msg":"user is deleted"}

def get_user_in_db(*,username: str,db:Session):
    user= db.query(User).filter(User.username==username).first()
    if not user:
        return "error"
    return {"username":user.username}

def update_user_username_in_db(current_username:str,data:Userupdateshcema, db:Session):
    is_correct= db.query(User).filter_by(username=current_username,password=data.password).first()
    if not is_correct:
        raise HTTPException(status_code=404, detail="user not found")
    return "operation was succesfull"