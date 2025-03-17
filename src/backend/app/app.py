from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import me
from api import recipes
from database.config import engine, database, Base
from core.settings import settings

from core.openid_config import azure_scheme
from fastapi import Security


app = FastAPI(
    swagger_ui_init_oauth={
        'usePkceWithAuthorizationCodeGrant': True,
        'clientId': settings.OPENAPI_CLIENT_ID,
    },
    dependencies=[Security(azure_scheme)]
)


app.include_router(me.router, prefix="/api")
app.include_router(recipes.router, prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)