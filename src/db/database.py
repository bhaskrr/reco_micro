from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from utils.globals import DATABASE_URL

# Creates an engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session
SessionLocal = sessionmaker(autoflush=False, bind=engine)

# Base class to create declarative objects(tables)
Base = DeclarativeBase()


def get_db():
    "Depenency to get DB session in routes."
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
