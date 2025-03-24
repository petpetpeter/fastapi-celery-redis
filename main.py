import time

import uvicorn as uvicorn
from fastapi import FastAPI

from src.config.celery_utils import create_celery
from src.routers import universities
from src.routers import line


def create_app() -> FastAPI:
    current_app = FastAPI(title="Asynchronous tasks processing with Celery and Redis",
                          description="Sample FastAPI Application to demonstrate Event "
                                      "driven architecture with Celery and Redis",
                          version="1.0.0", )

    current_app.celery_app = create_celery()
    current_app.include_router(universities.router)
    current_app.include_router(line.router)
    return current_app


app = create_app()
celery = app.celery_app


@app.middleware("http")
async def add_process_time_header(request, call_next):
    print('inside middleware!')
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(f'{process_time:0.4f} sec')
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)
