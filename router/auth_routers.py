from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from auth import create_access_token
from database import get_db
from models import UserDB
from schemas import UserRegister
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(UserDB).filter(UserDB.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    if user.password != user.confirm_password:
        raise HTTPException(status_code=409,detail="password mismatched")
    

    if len(user.mobile_number) != 10:
        raise HTTPException(status_code=400,detail="mobile number should be atleast 10 digit")

    new_user = UserDB(username=user.username, password=user.password,mobile_number=user.mobile_number)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully", "username": new_user.username}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = form_data.username
    password = form_data.password

    db_user = db.query(UserDB).filter(UserDB.username == username).first()
    if not db_user or db_user.password != password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token(data={"sub": db_user.username, "role": db_user.role})
    response = JSONResponse(content={"access_token": token, "token_type": "bearer"})
    response.set_cookie(key="access_token", value=token, httponly=True)
    return response
