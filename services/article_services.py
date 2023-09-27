from services.validate import check_article
from sqlalchemy.orm import Session

from core.models.article import Article
from core.schema.article import ArticleCreateSchema, ArticleUpdateSchema



def get_article(db: Session, article_id: int):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    check_article(db_article, article_id)
    return db_article


def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Article).offset(skip).limit(limit).all()


def create_new_article(db: Session, article: ArticleCreateSchema):
    db_article = Article(name=article.name, description=article.description, 
                         link=article.link, created_at=article.created_at,
                         update_at=article.update_at)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def update_article(db: Session, article_id: int , article: ArticleUpdateSchema):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    check_article(db_article, article_id)
    for var, value in vars(article).items():
        setattr(db_article, var, value) if value else None
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
