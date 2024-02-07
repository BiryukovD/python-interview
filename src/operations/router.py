from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from operations.models import Question
from operations.shemas import Question as Question_schema
from sqlalchemy.sql.expression import func


router = APIRouter(
    prefix="",
    tags=["Operation"]
)

@router.get('/question')
async def get_random_question(session: AsyncSession = Depends(get_async_session)):
    query = select(Question).order_by(func.random())
    result = await session.execute(query)
    return result.scalars().first()

@router.post('/question')
async def post_new_question(question: Question_schema, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Question).values(**question.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.delete('/question')
async def delete_question(question_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Question).where(Question.id == question_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.put('/question')
async def change_question(question: Question_schema, question_id: int, session: AsyncSession = Depends(get_async_session)):

    query = select(Question).where(Question.id == question_id)
    result = await session.execute(query)
    question_db = result.scalars().first()
    if question_db == None:
        raise HTTPException(status_code=404, detail={"status": "error", "detail": f"Вопрос с id = {question_id} не найден!"})
    else:
        question_db.question = question.question
        question_db.answer = question.answer
        question_db.additional_material = question.additional_material
        await session.commit()
        return {"status": "success"}
