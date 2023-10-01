from fastapi import APIRouter, Depends, Header, status
from services.token_services import check_valid_token
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


@router.post('/category_article', response_model=CategoryArticleSchema, status_code=status.HTTP_201_CREATED, tags=['CategoryArticle'])
async def create_article(article: CategoryArticleCreateSchema, 
                         db: Session = Depends(get_db),
                         authorization: str = Header(...)):
    check_valid_token(authorization)
    response = create_category_article(db, article)
    return response


@router.get('/category_article', response_model=list[CategoryArticleSchema], tags=['CategoryArticle'])
async def read_category_articles(db: Session = Depends(get_db), 
                                 authorization: str = Header(...)):
    check_valid_token(authorization)
    response = get_category_articles(db)
    return response


@router.get('/category_article/{category_article_id}', response_model=CategoryArticleSchema, tags=['CategoryArticle'])
async def read_category_article(category_article_id: int, 
                                db: Session = Depends(get_db), 
                                authorization: str = Header(...)):
    check_valid_token(authorization)
    response = get_category_article(db, category_article_id)
    return response


@router.patch('/category_article/{category_article_id}', response_model=CategoryArticleSchema, tags=['CategoryArticle'])
async def patch_article(category_article_id: int, 
                        category_article: CategoryArticleUpdateSchema, 
                        db: Session = Depends(get_db), 
                        authorization: str = Header(...)):
    check_valid_token(authorization)
    response = update_category_article(db, category_article_id, category_article)
    return response


@router.delete('/category_article/{category_article_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['CategoryArticle'])
async def delete_article(category_article_id: int, 
                         db: Session = Depends(get_db), 
                         authorization: str = Header(...)):
    check_valid_token(authorization)
    response = destroy_category_article(db, category_article_id)
