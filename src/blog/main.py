from fastapi import FastAPI
from blog import schemas
from blog import models
from blog.database import engine

app = FastAPI()
print("Creating tables...")
models.Base.metadata.create_all(engine)
print("Tables created.")


@app.post('/blog')
def create(request: schemas.Blog):
    return request

