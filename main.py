from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'blog list'}

@app.get('')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('src/blog/unpublished')
def unpublished():
    # fetch unpublished blogs
    return {'data': 'all unpublished blogs'}

@app.get('src/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

@app.get('src/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('')
def create_blog(blog: Blog):
    # create blog
    return {'data': 'Blog is created with title {blog.title}'}
