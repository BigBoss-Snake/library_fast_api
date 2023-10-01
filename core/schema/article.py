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
    categorys: list[int]

    class Config:
        orm_mode = True


class ArticleUpdateSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    link: str | None = None
    categorys: list[int] | None = None


class CategoryArticleCreateSchema(BaseModel):
    name: str
    articles: list[int]

    class Config:
        orm_mode = True

class CategoryArticleUpdateSchema(BaseModel):
    name: str | None = None
    articles: list[int] | None = None