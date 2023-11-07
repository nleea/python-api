from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .endpoints.router import api_router
from .core.settings import settings

# Instancia de fastAPI
app = FastAPI()

# Para permitir la conexion de aplicaciones
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Rutas creadas
app.include_router(api_router, prefix=settings.API_V1_STR)
