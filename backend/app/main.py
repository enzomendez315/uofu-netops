from fastapi import FastAPI
from app.routers import switches

app = FastAPI()

app.include_router(switches.router)
