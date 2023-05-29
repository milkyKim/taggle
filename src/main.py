from fastapi import FastAPI
from tag import tag_router
from resource import resource_router

app = FastAPI()

app.include_router(tag_router.router)
app.include_router(resource_router.router)
