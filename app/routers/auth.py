from msilib import schema
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(user_credentails:schemas.UserLogin, db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentails"
        )

    if not utils.verify_password(user_credentails.password, user.password):
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentails"
        )

    #create a token and return it
    return {"Token":"Token Generated"}