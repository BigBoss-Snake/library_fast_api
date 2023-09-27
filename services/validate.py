from fastapi import HTTPException

def check_category_article(category_article, id):
    if not category_article:
        raise HTTPException(status_code=404, detail=f"Category article with id {id} not found")
    

def check_article(article, id):
    if not article:
        raise HTTPException(status_code=404, detail=f"Article with id {id} not found")