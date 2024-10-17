from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from db import models
from db.database import engine
from exceptions import StoryException
from router import blog_get, user, article, product
from auth import authentication
from router import blog_post
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418,
                        content={'detail': exc.name})

models.Base.metadata.create_all(engine)


origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)