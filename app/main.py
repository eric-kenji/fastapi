
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote

# create postgres tables using sqlalchemy
# models.Base.metadata.create_all(bind=engine)

# init FastAPI
app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include post router
app.include_router(post.router)

# include user router
app.include_router(user.router)

# include authentication router
app.include_router(auth.router)

# include vote router
app.include_router(vote.router)

# root page
@app.get("/")
def root():
    return {"message": "Hello World!!!"}



