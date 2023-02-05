from typing import Generator

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Museum


router = APIRouter()


def get_db() -> Generator[SessionLocal, None, None]:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get('/')
async def search_museum(
    q: str, db: Session = Depends(get_db)
):
    title_query = db.query(Museum).filter(Museum.title.contains(q))
    content_query = db.query(Museum).filter(Museum.content.contains(q))
    result = title_query.union(content_query)
    return result.all()
