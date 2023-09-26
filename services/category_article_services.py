from sqlalchemy.orm import Session

from core.models.article import CategoryArticle
from core.schema.article import ArticleSchema


def get_category_article(db: Session, categor_article_id: int):
    return db.query(CategoryArticle).filter(CategoryArticle.id == categor_article_id).first()


def get_category_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoryArticle).offset(skip).limit(limit).all()


def create_category_article(db: Session, category_article: ArticleSchema):
    db_category_article = CategoryArticle(**category_article)
    db.add(db_category_article)
    db.commit()
    db.refresh(db_category_article)
    return db_category_article
