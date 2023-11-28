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
    return minecraft.start_server(server)

@router.get("/{server}/stop")
async def stop_server(server: str, force: bool | None = None):
    force = False if force is None else force
    return minecraft.stop_server(server, force)

@router.get("/{server}/restart")
async def restart_server (server: str, force: bool | None = None):
    force = False if force is None else force
    return minecraft.restart_server(server, force)

@router.get("/{server}/status")
async def server_status(server: str):
    return minecraft.server_status(server)