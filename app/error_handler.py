# app/error_handler.py

from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

def register_exception_handlers(app):

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail}
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc):
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid request format"}
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc):
        return JSONResponse(
            status_code=500,
            content={"error": "Internal Server Error"}
        )
