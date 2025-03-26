from fastapi import FastAPI
from app.routers import switch

app = FastAPI()

app.include_router(switch.router)
