from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from services.user_services import (
        create_user,
        check_user
    )
from core.schema.user import UserCreateSchema, UserSchema, SigninUserSchema


router = APIRouter()

@router.post('/signup', response_model=UserSchema, tags=['User'])
async def signup(user: UserCreateSchema, db: Session = Depends(get_db)):
    response = create_user(db, user)
    return response


@router.post('/signin', response_model=SigninUserSchema, tags=['User'])
async def signin(user: UserCreateSchema, db: Session = Depends(get_db)):
    response = check_user(db, user)
    return response
