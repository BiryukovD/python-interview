from fastapi import FastAPI
# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
# from redis import asyncio as aioredis
from operations.router import router as router_app
# from tasks.router import router as router_tasks
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Example App"
)

app.include_router(router_app)


origins = [
    "http://45.9.40.200:7777",
    "http://python-interview.ru"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)



# operations.include_router(router_tasks)


# @operations.on_event("startup")
# async def startup_event():
#     redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

