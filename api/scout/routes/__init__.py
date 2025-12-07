from fastapi import APIRouter

from . import mapping

api_router = APIRouter()

api_router.include_router(mapping.router, prefix="/mapping", tags=["mapping"])