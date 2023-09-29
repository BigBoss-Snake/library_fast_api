import datetime

from pydantic import BaseModel

class ArticleItemSchema(BaseModel):
    id: int
    name: str
    description: str
    link: str 
    created_at: datetime.datetime
    update_at: datetime.datetime



class CategoryArticleItemSchema(BaseModel):
    id: int
    name: str


class ArticleSchema(ArticleItemSchema):
    categorys: list[CategoryArticleItemSchema] = []

    class Config:
        orm_mode = True


class CategoryArticleSchema(CategoryArticleItemSchema):
    articles: list[ArticleItemSchema] = []

    class Config:
        orm_mode = True


class ArticleCreateSchema(BaseModel):
    name: str
    description: str
    link: str 
    category_article: list[int]

    class Config:
        orm_mode = True


class ArticleUpdateSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    link: str | None = None
    category_article: list[int] | None = None


class CategoryArticleCreateSchema(BaseModel):
    name: str
    article: list[int]

    class Config:
        orm_mode = True

class CategoryArticleUpdateSchema(BaseModel):
    name: str | None = None
    article: list[int] | None = None