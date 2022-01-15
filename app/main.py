from .database import engine
from .models import Base
from fastapi import FastAPI
from .routes import blog

app = FastAPI()

app.include_router(blog.router)

Base.metadata.create_all(engine)
