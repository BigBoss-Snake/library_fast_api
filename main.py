from fastapi import FastAPI
from core.models import user, article
from core.database import engine
from routers.article import router as article_route
from routers.category_article import router as categoty_article_route
from routers.user import router as user_router

user.Base.metadata.create_all(bind=engine)
article.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user_router)
app.include_router(article_route)
app.include_router(categoty_article_route)
