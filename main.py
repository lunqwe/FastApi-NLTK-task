import uvicorn
from fastapi import FastAPI
from .routers import routers

app = FastAPI()
app.include_router(router=routers.router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, workers=3)