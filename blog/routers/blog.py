from fastapi import Depends, status, Response, APIRouter
from typing import List
from .. import schemas
from sqlalchemy.orm import Session
from ..database import *
from ..repository import blog

router = APIRouter(
    tags=['Blogs'],
    prefix="/blog"
)

@router.get('/', response_model= List[schemas.ShowBlog])
def get_all(db: Session= Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session= Depends(get_db)):
    return blog.create(request, db)

@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def get_one(id:int, response:Response, db: Session= Depends(get_db)):
    return blog.get_one(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schemas.Blog, db: Session= Depends(get_db)):
    return blog.update(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session= Depends(get_db)):
    return blog.destroy(id, db)

