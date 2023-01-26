from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    blogs= db.query(models.Blog).all()
    return blogs

def create(request, db: Session):
    #request is not a pydentic thing so we have to convert it 
    new_blog = models.Blog(
        title=request.title, 
        body=request.body,
        user_id= 1 #request.creator
        )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def updtae(id:int, request:schemas.Blog, db: Session):
    db_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not db_blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'blog with id {id} not found' 
        )
    db_blog.update(request.dict())
    db.commit()
    return 'updated'

def get_one(id:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
        # response.status_code= status.HTTP_404_NOT_FOUND
        # return {"details":f"Blog with id {id} not found"}
    return blog

def destroy(id:int, db: Session):
    db_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not db_blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'blog with id {id} not found' 
        )
    db_blog.delete(synchronize_session=False)
    db.commit()
    return "deleted"