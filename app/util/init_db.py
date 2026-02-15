from app.core.database import engine, base
from app.db.model.users import Users

def create_tables():
    base.metadata.create_all(engine)