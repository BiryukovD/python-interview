from pydantic import BaseModel
class Question(BaseModel):
    question: str
    answer: str
    additional_material: str