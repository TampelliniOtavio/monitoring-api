from fastapi import APIRouter
import subprocess

router = APIRouter(
    prefix="/minecraft",
    tags=["minecraft"],
    responses={404: {"description": "Não Encontrado"}},
)

@router.get("/server/list")
async def list_all_servers():
    cmd = ["msm", "server list"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout = result.stdout.decode('utf-8')
    return stdout