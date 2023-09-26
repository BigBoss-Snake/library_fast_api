from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from services.article_services import get_articles, get_article
from core.schema.article import ArticleSchema


router = APIRouter()


@router.get('/article', response_model=list[ArticleSchema], tags=['Article'])
async def read_articles(db: Session = Depends(get_db)):
    response = get_articles(db)
    return response


@router.get('/article/{article_id}', response_model=ArticleSchema, tags=['Article'])
async def read_article(article_id: int, db: Session = Depends(get_db)):
    response = get_article(db, article_id=article_id)
    return response