from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.similar_chip import router as similar_chip_router
from app.middleware.error_handler import add_error_handlers

def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Or specify your frontend's URL(s)
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(similar_chip_router, prefix="/api")
    add_error_handlers(app)
    return app

app = create_app()
