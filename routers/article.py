from fastapi import APIRouter, Depends, Header, status
from services.token_services import check_valid_token
from sqlalchemy.orm import Session

from core.database import get_db
from services.article_services import (
    get_articles,
    get_article,
    create_new_article,
    update_article,
    destroy_article
    )
from core.schema.article import (
    ArticleCreateSchema,
    ArticleSchema,
    ArticleUpdateSchema
)


router = APIRouter()


@router.post('/article', response_model=ArticleSchema, status_code=status.HTTP_201_CREATED, tags=['Article'])
async def create_article(article: ArticleCreateSchema, 
                         db: Session = Depends(get_db), 
                         authorization: str = Header(...)):
    check_valid_token(authorization)
    response = create_new_article(db, article)
    return response


@router.get('/article', response_model=list[ArticleSchema], tags=['Article'])
async def read_articles(filter_by_category: str | None = None,
                        db: Session = Depends(get_db),
                        authorization: str = Header(...),
                        ):
    check_valid_token(authorization)
    response = get_articles(db, filter_by_category)
    return response


@router.get('/article/{article_id}', response_model=ArticleSchema, tags=['Article'])
async def read_article(article_id: int, 
                       db: Session = Depends(get_db), 
                       authorization: str = Header(...)):
    check_valid_token(authorization)
    response = get_article(db, article_id=article_id)
    return response


@router.patch('/article/{article_id}', response_model=ArticleSchema, tags=['Article'])
async def patch_article(article_id: int, 
                        article: ArticleUpdateSchema, 
                        db: Session = Depends(get_db), 
                        authorization: str = Header(...)):
    check_valid_token(authorization)
    response = update_article(db, article_id, article)
    return response


@router.delete('/article/{article_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Article'])
async def delete_article(article_id: int, 
                         db: Session = Depends(get_db), 
                         authorization: str = Header(...)):
    check_valid_token(authorization)
    response = destroy_article(db, article_id=article_id)
