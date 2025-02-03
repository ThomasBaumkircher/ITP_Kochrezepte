from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer
from core.settings import settings


azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id=settings.APP_CLIENT_ID,
    tenant_id=settings.TENANT_ID,
    scopes=settings.SCOPES,
    redirect_uri=settings.BACKEND_CORS_ORIGINS[0] + "/callback",
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Load OpenID config on startup.
    """
    await azure_scheme.openid_config.load_config()
    yield