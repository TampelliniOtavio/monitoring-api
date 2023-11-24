import re
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

    filtered = list(filter(lambda x: x != "", result))

    def format(row):
        reg_status = "(\[.*\])"
        reg_server_name = "(\".*\")"
        reg_message = "(\..*\.)"

        status = re.search(reg_status, row).group()
        server_name = re.search(reg_server_name, row).group()
        message = re.search(reg_message, row).group()

        return {
            "status": status[1:len(status) - 1],
            "serverName": server_name[1:len(server_name) - 1],
            "message": message[2:len(message) - 1]
        }

    return [format(x) for x in filtered]