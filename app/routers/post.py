
from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db


router = APIRouter()
#We create application specific routes and then merge in main route which
# is app in our case shown in main.py
#router = APIRouter(prefix="/posts")

#lets say we have many route url like /posts then, to avoid repetition we
#can put a prefix as shown below
#router = APIRouter(prefix="/posts") and in the route function where route is
#"/posts" we just put "/"

@router.get("/posts")
def get_posts(db: Session = Depends(get_db), limit: int = 10, skip:int =0,
        search:Optional[str] = ""):
    # cursor.execute("""Select * from posts""")
    # posts = cursor.fetchall()
    print(search)
    posts = db.query(models.Post).filter(
        models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts


# @app.get("/sqlalchemy")
# def test_post(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data":posts}


@router.get("/view_posts/{id}")
# we use Response to set the correct status code to be 
#shown in postman, if data with given id is not found
def get_post_byID(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""Select * from posts where id = %s""",(str(id)))
    # post_data = cursor.fetchone()

    post_data = db.query(models.Post).filter(models.Post.id == id).first()
    # print(post_data)
    if not post_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} was not found"
        )
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"Message":f"Post with {id} was not found"}
    return post_data


@router.post("/create_post", status_code= status.HTTP_201_CREATED)
def createposts(post : schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""Insert into posts(title, content, published)
    # values (%s,%s,%s) returning *""", (post.title, post.content, post.published))

    # new_post = cursor.fetchone()
    # conn.commit()
    # new_post = models.Post(title=post.title, content=post.content, 
    #             published=post.published)
    post_dict = post.dict()
    post_dict.update({"owner_id":post.owner_id})
    new_post = models.Post(**post_dict)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletepost(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""delete from posts where id = %s returning *""",(str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)
    
    if post.first() == None:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} was not found"
        )



    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)     


@router.put("/updatepost/{id}")
def putrequest(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):

    # cursor.execute("""Update posts set title= %s, content=%s, published=%s
    # where id=%s returning *""", 
    # (post.title, post.content, post.published,str(id)))

    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()

    if updated_post == None:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with {id} was not found"
        )
    post_query.update(post.dict(), synchronize_session=False)

    db.commit()
    return post_query.first()