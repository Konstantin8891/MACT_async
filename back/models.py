from sqlalchemy import Integer, DateTime, Column, Text

from database import Base


class Museum(Base):
    __tablename__ = 'museums'
    id = Column(Integer, primary_key=True, index=True)
    service = Column(Text)
    link = Column(Text)
    title = Column(Text)
    content = Column(Text)
    added = Column(DateTime)
