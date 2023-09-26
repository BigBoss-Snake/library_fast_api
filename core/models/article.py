from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, Table
from core.database import Base
from sqlalchemy.sql import func


article__category_article = Table('article__category_article', Base.metadata,
    Column('article_id', ForeignKey('article.id'), primary_key=True),
    Column('category_article_id', ForeignKey('caregory_article.id'), primary_key=True)
)

class CategoryArticle(Base):
    __tablename__ = 'caregory_article'
    id  = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Article(Base):
    __tablename__ = 'article'
    id  = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    link = Column(Text)
    created_at = Column(DateTime(timezone=True), onupdate=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())


