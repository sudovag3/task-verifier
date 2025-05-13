from fastapi import FastAPI, Request
import time, logging

from .core.logger import setup_logging
from .api.routes import router as api_router


def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(
        title="Task verifier API",
        version="1.0.0",
        docs_url="/docs",
        openapi_url="/openapi.json",
    )

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration = (time.perf_counter() - start) * 1000
        logging.getLogger().info(
            f"{request.method} {request.url.path} - {response.status_code} {round(duration,1)} ms",
        )
        return response

    app.include_router(api_router)
    return app
