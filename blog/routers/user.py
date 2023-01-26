from fastapi import Depends, status, Response, HTTPException, APIRouter
from .. import schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..database import *
from ..repository import user

router = APIRouter(
    tags=["Users"],
    prefix="/user"
)


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session= Depends(get_db)): 
    return user.create(request, db)

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session= Depends(get_db)):
    return user.get(id, db)

