from fastapi import APIRouter, Depends
from fastapi_azure_auth.user import User
from typing import List

from models.recipe import RecipeResponse
from crud.recipes import RecipeCRUD
from crud.dependencies import get_recipe_crud

from core.openid_config import AzureScheme


router = APIRouter(prefix="/me", tags=["me"])


@router.get("", response_model=User)
async def protected(current_user: User = Depends(AzureScheme.azure_scheme)):
    return current_user


@router.get("/recipes", response_model=List[RecipeResponse])
async def get_recipes(
    current_user: User = Depends(AzureScheme.azure_scheme),
    db: RecipeCRUD = Depends(get_recipe_crud)
):
    return [RecipeResponse(**vars(recipe)) for recipe in await db.get_user_recipes(current_user.email)]