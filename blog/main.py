from fastapi import FastAPI
from . import schemas
from . import models
from .database import engine

app = FastAPI()
print("Creating tables...")
models.Base.metadata.create_all(engine)
print("Tables created.")


@app.post('/blog')
def create(request: schemas.Blog):
    return request

