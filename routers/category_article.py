from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from services.category_article_services import get_category_article, get_category_articles
from core.schema.article import CategoryArticleSchema


router = APIRouter()


@router.get('/category_article', response_model=list[CategoryArticleSchema], tags=['CategoryArticle'])
async def read_category_articles(db: Session = Depends(get_db)):
    response = get_category_articles(db)
    return response


@router.get('/article/{category_article_id}', response_model=CategoryArticleSchema, tags=['CategoryArticle'])
async def read_category_article(category_article_id: int, db: Session = Depends(get_db)):
    response = get_category_article(db, category_article_id=category_article_id)
    return response