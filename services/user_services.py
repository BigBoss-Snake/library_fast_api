from sqlalchemy.orm import Session
from fastapi import HTTPException

from services.token_services import generate_access_token
from core.schema.user import UserCreateSchema
from core.models.user import User
from .validate import validate_email, check_user_password


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreateSchema):
    validate_email(db, user.email)
    fake_hashed_password = user.password + 'notreallyhashed'
    db_user = User(email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def check_user(db: Session, user: UserCreateSchema):
    db_user = get_user_by_email(db, user.email)
    if not db_user:
        raise HTTPException(status_code=422, detail=f"Email or password entered incorrectly")
    elif check_user_password(db_user.password, user.password):
        raise HTTPException(status_code=422, detail=f"Email or password entered incorrectly")
    generate_access_token(db_user)
    response = {
                   'access_token': generate_access_token(db_user), 
                   'email': db_user.email
               }
    return response
