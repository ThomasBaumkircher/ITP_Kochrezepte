from fastapi import APIRouter, Depends
from fastapi_azure_auth.user import User

from core.openid_config import azure_scheme


router = APIRouter(prefix="/me", tags=["me"])


@router.get("", response_model=User)
async def protected(current_user: User = Depends(azure_scheme)):
    return current_user
