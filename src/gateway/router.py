from fastapi import APIRouter, Depends
from starlette.requests import Request
from src.gateway.service import TokenService, init_token_service

gateway_router = APIRouter(prefix="/gateway", tags=["gateway"])


@gateway_router.get("/verify/")
async def verify_token_router(request: Request, service: TokenService = Depends(
                              init_token_service)):
    """Роутер проверки токена"""
    return await service.verify_token(request)
