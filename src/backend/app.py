from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware

from api import me
from database.config import engine, database, Base
from core.settings import settings
from core.openid_config import azure_scheme


app = FastAPI(
    swagger_ui_oauth2_redirect_url='/oauth2-redirect',
    swagger_ui_init_oauth={
        'usePkceWithAuthorizationCodeGrant': True,
        'clientId': settings.OPENAPI_CLIENT_ID,
    },
    dependencies=[Security(azure_scheme)])

app.include_router(me.router, prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
