from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Blog(BaseModel):
    id: int
    title: str
    published: Optional[bool]


blogs = {
    0:{
        'name': 'blog1',
        'author': 'author1'
    },
    1:{
        'name': 'blog2',
        'author': 'author2'
    },
}

@app.get('/') 
def index():
    return {'data': {
        'name': 'Nesrine'
    }}

@app.get('/blog-name/{id}/name') 
def get_name(id: int):
    return {'data': blogs[id]['name']}

@app.get('/blog/unpublished')
def show():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': blogs[id]}

@app.get('/blog-on-cond')
def cond(limit: int, published: bool=False):
    if published:
        return {'data': f'give me {limit} of published blogs'}
    return {'data': f'give me {limit} of unpublished blogs'}

@app.post('/create')
def create(blog: Blog):
    return {'data': f'blog created with a title of {blog.title}'}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
