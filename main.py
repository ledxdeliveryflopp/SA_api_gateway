from fastapi import FastAPI
from src.gateway.router import gateway_router

gateway = FastAPI()

gateway.include_router(gateway_router)
