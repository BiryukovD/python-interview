from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    added_at = Column(TIMESTAMP, default=datetime.utcnow)
    question = Column(String)
    answer = Column(String)
    additional_material = Column(String)



