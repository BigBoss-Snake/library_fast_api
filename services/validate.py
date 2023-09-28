from fastapi import HTTPException
from sqlalchemy.orm import Session
from core.models.user import User

def check_category_article(category_article, id):
    if not category_article:
        raise HTTPException(status_code=404, detail=f"Category article with id {id} not found")
    

def check_article(article, id):
    if not article:
        raise HTTPException(status_code=404, detail=f"Article with id {id} not found")


def validate_email(db: Session, email: str) -> str:
    chech_email = db.query(User).filter(User.email == email).first()
    if chech_email:
        raise HTTPException(status_code=422, detail=f"Email {email} is already in use")


def check_user_password(db_password: str, request_password: str) -> bool:
    request_password = request_password + "notreallyhashed"
    return db_password != request_password 
