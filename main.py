from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/blog/all")
def get_all_blogs():
    return {"message": "All blogs provided"}


@app.get("/blog/{id}")
def get_blog(id: int):
    return {"message": f"Blog with id {id}"}
