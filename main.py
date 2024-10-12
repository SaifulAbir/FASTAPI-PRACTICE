from fastapi import FastAPI
from db import models
from db.database import engine
from router import blog_get
from router import blog_post


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


models.Base.metadata.create_all(engine)