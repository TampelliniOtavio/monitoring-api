from fastapi import FastAPI
from app.routers import minecraft, healthcheck

app = FastAPI()

app.include_router(minecraft.router)
app.include_router(healthcheck.router)

def main():
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)

if __name__ == "__main__":
    main()