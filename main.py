from fastapi import FastAPI
from psutil import virtual_memory, cpu_percent, disk_usage

app = FastAPI()

@app.get("/healthcheck")
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

def main():
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)

if __name__ == "__main__":
    main()