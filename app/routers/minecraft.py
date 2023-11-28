from fastapi import APIRouter
from app.services.minecraft import Minecraft

router = APIRouter(
    prefix="/minecraft",
    tags=["minecraft"],
    responses={404: {"description": "Não Encontrado"}},
)

minecraft = Minecraft()

@router.get("/server/list")
async def list_all_servers():
    return minecraft.list_all_servers()

@router.get("/{server}/start")
async def start_server(server: str):
    return minecraft.start_server()