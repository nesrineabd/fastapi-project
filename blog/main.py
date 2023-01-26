from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, blog, authentication

# create all models/tables found in models file
models.Base.metadata.create_all(engine)

tags_metadata = [
    {
        "name": "Authentication",
        "description": "login with JWT"
    },
    {
        "name": "Users",
        "description": "Operations with users",
    },

    {
        "name": "Blogs",
        "description": "Manage items",
    },
]
app = FastAPI(openapi_tags=tags_metadata)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)














# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=["blogs"])
# def create(blog: schemas.Blog, db: Session= Depends(get_db)):
#     #session is not a pydentic thing so we have to convert it 
#     new_blog = models.Blog(
#         title=blog.title, 
#         body=blog.body,
#         user_id= blog.creator
#         )
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog', response_model= List[schemas.ShowBlog], tags=["blogs"])
# def get_all(db: Session= Depends(get_db)):
    # blogs= db.query(models.Blog).all()
    # return blogs

# @app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=["blogs"])
# def show(id:int, response:Response, db: Session= Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Blog with id {id} not found"
#         )
#         # response.status_code= status.HTTP_404_NOT_FOUND
#         # return {"details":f"Blog with id {id} not found"}
#     return blog

# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
# def destroy(id:int, db: Session= Depends(get_db)):
#     db_blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not db_blog.first():
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f'blog with id {id} not found' 
#         )
#     db_blog.delete(synchronize_session=False)
#     db.commit()
#     return "delete done"

# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
# def update(id:int, blog:schemas.Blog, db: Session= Depends(get_db)):
#     db_blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not db_blog.first():
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f'blog with id {id} not found' 
#         )
#     db_blog.update(blog.dict())
#     db.commit()
#     return 'updated'

# @app.post("/user", response_model=schemas.ShowUser, tags=["users"])
# def create_user(user: schemas.User, db: Session= Depends(get_db)):
#     new_user = models.User(
#         name=user.name, 
#         email=user.email,
#         password= Hash.bcrypt(user.password)
#         )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get("/user/{id}", response_model=schemas.ShowUser, tags=["users"])
# def get_user(id: int, db: Session= Depends(get_db)):
    # user = db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"User with id {id} not found"
    #     )
    # return user


