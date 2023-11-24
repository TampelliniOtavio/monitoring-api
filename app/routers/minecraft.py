from fastapi import APIRouter
import os

router = APIRouter(
    prefix="/minecraft",
    tags=["minecraft"],
    responses={404: {"description": "Não Encontrado"}},
)

@router.get("/server/list")
async def list_all_servers():
    cmd = "/usr/local/bin/msm server list"
    result = os.popen(cmd).read().split("\n")
    return result