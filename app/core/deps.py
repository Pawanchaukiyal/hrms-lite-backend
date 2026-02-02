# Database session dependency
# Ensures session open and close per request

from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
