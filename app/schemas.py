from datetime import datetime 
from pydantic import BaseModel, EmailStr
#This schema/pydentic model define the structure of a request and response
#this ensures that the request will go through only if it has a title and 
#content in the body.


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    owner_id: int

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str


# class PostBase(BaseModel):
#     title: str
#     content : str
#     published: bool = True



# class PostCreate(PostBase):
#     pass


# #Here we are trying to define how the output of the api call should look like.
# class Post(PostBase):
#     id: int
#     created_at = datetime
#     class Config:
#         orm_mode:True


# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str


# class UserOut(BaseModel):
#     id: int
#     email: EmailStr

#     class Config:
#         orm_mode:True


# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str