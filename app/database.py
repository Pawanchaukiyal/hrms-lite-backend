# Database connection and session setup
# Handles PostgreSQL connection using SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(
    autoflush=False,
    bind=engine,
    autocommit=False
)

Base = declarative_base()