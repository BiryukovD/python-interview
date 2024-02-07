from httpx import AsyncClient


async def test_post_new_question(ac: AsyncClient):
    response = await ac.post("/question", json=
    {
        "question": "Что такое SOLID?",
        "answer": "Эти пять правил разработки ПО",
        "additional_material": "https://habr.com/ru/companies/productivity_inside/articles/505430/"
    })
    assert response.status_code == 200
    assert response.json()['status'] == 'succes'



async def test_get_random_question(ac: AsyncClient):
    response = await ac.get("/question")
    assert response.status_code == 200


async def test_put_pereval_by_id(ac: AsyncClient):
    response = await ac.put("/question/1", json=
    {
        "question": "Что такое REST?",
        "answer": "Архитектурный стил построения API",
        "additional_material": "https://habr.com/ru/articles/38730/"
    }
                              )
    assert response.status_code == 200
    assert response.json()['status'] == 'succes'


async def test_delete_question(ac: AsyncClient):
    response = await ac.delete("/question/1")
    assert response.status_code == 200
    assert response.json()['status'] == 'succes'


