from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import Blog

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get("")
async def get_all_fetch(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(blog: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
