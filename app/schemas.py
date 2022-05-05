from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

# base model for posts
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# model for received post 
class PostCreate(PostBase):
    pass

# model for sent user
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# model for sent post
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

# model for received user
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# model for received login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# model for token
class Token(BaseModel):
    access_token: str
    token_type: str 

class TokenData(BaseModel):
    id: Optional[str] = None

# model for vote
class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0,le=1)