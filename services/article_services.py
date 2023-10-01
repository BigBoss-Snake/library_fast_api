from .validate import check_article, check_category_article
from sqlalchemy.orm import Session
import datetime

from core.models.article import Article, CategoryArticle
from core.schema.article import ArticleCreateSchema, ArticleUpdateSchema



def get_article(db: Session, article_id: int):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    check_article(db_article, article_id)
    return db_article


def get_articles(db: Session, filter: int, skip: int = 0, limit: int = 100):
    if filter:
        response = db.query(Article).filter(Article.categorys.any(id=filter)).offset(skip).limit(limit).all()
    else:
        response = db.query(Article).offset(skip).limit(limit).all()
    return response


def create_new_article(db: Session, article: ArticleCreateSchema):
    db_article = Article(name=article.name, description=article.description, 
                         link=article.link, created_at=datetime.datetime.now(),
                         update_at=datetime.datetime.now())
    for category in article.categorys:
        db_category_article = db.query(CategoryArticle).filter(CategoryArticle.id == category).first()
        check_category_article(db_category_article, category)
        db_article.categorys.append(db_category_article)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def update_article(db: Session, article_id: int , article: ArticleUpdateSchema):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    check_article(db_article, article_id)
    for var, value in vars(article).items():
        if var != 'categorys':
            setattr(db_article, var, value) if value else None
    for category in article.categorys:
        db_category_article = db.query(CategoryArticle).filter(CategoryArticle.id == category).first()
        check_category_article(db_category_article, category)
        db_article.categorys.append(db_category_article)
    db_article.update_at = datetime.datetime.now()
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def destroy_article(db: Session, article_id: int):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    check_article(db_article, article_id)

    db.delete(db_article)
    db.commit()
    return db_article
