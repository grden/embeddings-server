from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

def add_error_handlers(app: FastAPI):
    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"detail": "An internal server error occurred."}
        ) 