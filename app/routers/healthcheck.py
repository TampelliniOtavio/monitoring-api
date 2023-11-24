from fastapi import APIRouter
from psutil import virtual_memory, cpu_percent, disk_usage

router = APIRouter(
    prefix="/healthcheck",
    tags=["healthcheck"],
    responses={404: {"description": "Não Encontrado"}},
)

@router.get("/")
async def get_healthckeck():
    disk_info = disk_usage("/")
    cpu_perc = cpu_percent()
    ram_info = virtual_memory()

    ram = {
        "total": f"{ram_info.total / 1024 / 1024 / 1024:.2f} GB",
        "avaliable": f"{ram_info.available / 1024 / 1024 / 1024:.2f} GB",
        "used": f"{ram_info.used / 1024 / 1024 / 1024:.2f} GB",
        "percentage": f"{ram_info.percent}%"
    }

    disk = {
        "total": f"{disk_info.total / 1024 / 1024 / 1024:.2f} GB",
        "avaliable": f"{disk_info.free / 1024 / 1024 / 1024:.2f} GB",
        "used": f"{disk_info.used / 1024 / 1024 / 1024:.2f} GB",
        "percentage": f"{disk_info.percent}%"
    }

    cpu = {
        "percentage": f"{cpu_perc}%"
    }

    return {
        "ram": ram,
        "disk": disk,
        "cpu": cpu
    }