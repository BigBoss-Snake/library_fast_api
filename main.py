from fastapi import FastAPI
from core.models import user, article
from core.database import engine, SessionLocal
from routers.article import router as article_route
from routers.category_article import router as categoty_article_route

user.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(article_route)
app.include_router(categoty_article_route)