from pydantic import BaseModel


class Blog(BaseModel):
    title: str

    class Config:
        orm_mode = True
