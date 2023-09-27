from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from services.category_article_services import (
    get_category_article,
    get_category_articles,
    create_category_article,
    update_category_article,
    destroy_category_article)
from core.schema.article import (
    CategoryArticleSchema,
    CategoryArticleCreateSchema,
    CategoryArticleUpdateSchema
)


router = APIRouter()


@router.post('/category_article', response_model=CategoryArticleSchema, tags=['CategoryArticle'])
async def create_article(article: CategoryArticleCreateSchema, db: Session = Depends(get_db)):
    response = create_category_article(db, article)
    return response


@router.get('/category_article', response_model=list[CategoryArticleSchema], tags=['CategoryArticle'])
async def read_category_articles(db: Session = Depends(get_db)):
    response = get_category_articles(db)
    return response


@router.get('/category_article/{category_article_id}', response_model=CategoryArticleSchema, tags=['CategoryArticle'])
async def read_category_article(category_article_id: int, db: Session = Depends(get_db)):
    response = get_category_article(db, category_article_id)
    return response


@router.patch('/category_article', response_model=CategoryArticleSchema, tags=['CategoryArticle'])
async def patch_article(article_id: int, article: CategoryArticleUpdateSchema, db: Session = Depends(get_db)):
    response = update_category_article(db, article_id, article)
    return response


@router.delete('/category_article/{category_article_id}', response_model=CategoryArticleSchema, tags=['CategoryArticle'])
async def delete_article(category_article_id: int, db: Session = Depends(get_db)):
    response = destroy_category_article(db, category_article_id)
    return response
