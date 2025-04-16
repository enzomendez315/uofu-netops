from fastapi import APIRouter

from app.api.routes import switches

api_router = APIRouter()
api_router.include_router(switches.router, prefix="/api/v1")