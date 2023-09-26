from sqlalchemy.orm import Session

from core.models.article import Article
from core.schema.article import ArticleSchema


def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()


def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Article).offset(skip).limit(limit).all()


def create_article(db: Session, article: ArticleSchema):
    db_article = Article(**article)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
