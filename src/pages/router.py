from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.database import SessionLocal
from src.posts import models, schemas
from src.posts.models import post

router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)

templates = Jinja2Templates(directory="templates")


@router.get('/about', response_class=HTMLResponse)
def about_get_page(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {"request": request}
    )


@router.get('/portfolio', response_class=HTMLResponse)
def portfolio_get_page(request: Request):
    return templates.TemplateResponse(
        'portfolio.html',
        {"request": request}
    )


@router.get('/contact', response_class=HTMLResponse)
def contact_get_page(request: Request):
    return templates.TemplateResponse(
        'contact.html',
        {"request": request}
    )


# ORM
def get_database_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/posts", response_class=HTMLResponse)
def post_get_page(request: Request, page: int = 1, limit: int = 2,
                  db: Session = Depends(get_database_session)):
    skip = (page - 1)
    post_list = db.query(post).offset(skip).limit(limit).all()
    count = db.query(models.post).count()
    for i in range(1, count + 1, 3):
        skip = ((page - 1) + i) - 3
    url = f"?page={skip + 1}&limit={limit}"
    return templates.TemplateResponse("post.html", {"request": request, "post": post_list,
                                                    "total": count, "page": page, "skip": skip, "per_page": limit,
                                                    "url": url
                                                    })

