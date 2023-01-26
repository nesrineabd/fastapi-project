from fastapi import Depends, HTTPException, status
from .. import models, schemas
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..database import *


def create(user: schemas.User, db: Session= Depends(get_db)):
    new_user = models.User(
        name=user.name, 
        email=user.email,
        password= Hash.bcrypt(user.password)
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id:int, db: Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    return user

