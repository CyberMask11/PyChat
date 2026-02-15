from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL = "postgresql://graymask:neveahbott5@localhost:5432/pychat"
engine = create_engine(URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()