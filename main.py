from fastapi import FastAPI
from typing import Optional
from enum import Enum
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# @app.get("/blog/all")
# def get_all_blogs():
#     return {"message": "All blogs provided"}


@app.get("/blog/all")
def get_all_blogs(page = 1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on {page}"}


@app.get("/blog/{id}/comments/{comment_id}")
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"message": f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type is {type.value}"}


@app.get("/blog/{id}")
def get_blog(id: int):
    return {"message": f"Blog with id {id}"}
