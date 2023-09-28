from services.validate import check_category_article
from sqlalchemy.orm import Session

from core.models.article import CategoryArticle
from core.schema.article import CategoryArticleCreateSchema, CategoryArticleUpdateSchema




def get_category_article(db: Session, category_article_id: int):
    db_category_article = db.query(CategoryArticle).filter(CategoryArticle.id == category_article_id).first()
    check_category_article(db_category_article, category_article_id)
    return db_category_article


def get_category_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoryArticle).offset(skip).limit(limit).all()


def create_category_article(db: Session, category_article: CategoryArticleCreateSchema):
    db_category_article = CategoryArticle(name=category_article.name)
    db.add(db_category_article)
    db.commit()
    db.refresh(db_category_article)
    return db_category_article


def update_category_article(db: Session, category_article_id: int , category_article: CategoryArticleUpdateSchema):
    db_category_article = db.query(CategoryArticle).filter(CategoryArticle.id == category_article_id).first()
    check_category_article(db_category_article, category_article_id)

    db_category_article.name = category_article.name
    db.add(db_category_article)
    db.commit()
    db.refresh(db_category_article)
    return db_category_article


def destroy_category_article(db: Session, category_article_id: int):
    db_category_article = db.query(CategoryArticle).filter(CategoryArticle.id == category_article_id).first()
    check_category_article(db_category_article, category_article_id)

    db.delete(db_category_article)
    db.commit()
    return db_category_article
