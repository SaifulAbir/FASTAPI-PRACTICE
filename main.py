from fastapi import FastAPI
from router import blog_get


app = FastAPI()
app.include_router(blog_get.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
