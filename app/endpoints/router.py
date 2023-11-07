from fastapi import APIRouter
from .api import router

api_router = APIRouter()

api_router.include_router(router, prefix="/data")