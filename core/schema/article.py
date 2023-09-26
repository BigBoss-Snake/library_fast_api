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
    category_article: list[CategoryArticleItemSchema] = []

    class Config:
        orm_mode = True


class CategoryArticleSchema(CategoryArticleItemSchema):
    article: list[ArticleItemSchema] = []

    class Config:
        orm_mode = True
