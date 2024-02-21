from .database import SessionLocal


def get_db():
    """
    Method for configuring database
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
