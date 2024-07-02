from datetime import datetime

from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from src.database import engine, SessionLocal
from src.pages.router import router as router_pages
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.posts import models
from src.posts.models import metadata, post

app = FastAPI()
app.include_router(router_pages)
metadata.create_all(bind=engine)

# Home page
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def get_home_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )


# 404
def not_found_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse(
        request=request, status_code=404, name="404.html"
    )
# Register the error handler using the app.exception_handler decorator
@app.exception_handler(404)
def not_found_exception_handler(request: Request, exc: HTTPException):
    return not_found_error(request, exc)






