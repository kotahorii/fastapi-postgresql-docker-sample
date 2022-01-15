from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://fastapi_traefik:fastapi_traefik@db:5432/fastapi_traefik"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()


def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()
