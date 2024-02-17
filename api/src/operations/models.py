from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import TIMESTAMP, Column, Integer, String
class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    added_at = Column(TIMESTAMP, default=datetime.utcnow)
    question = Column(String)
    answer = Column(String)
    additional_material = Column(String)



