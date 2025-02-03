from api.api import GenericRouter
from crud.recipes import recipe_crud
from models.recipe import RecipePost, RecipePatch, RecipeResponse

from fastapi import Depends
from core.openid_config import azure_scheme
from fastapi_azure_auth.user import User


class RecipeRouter(GenericRouter):
    def __init__(self) -> None:
        super().__init__(recipe_crud, RecipePost, RecipePatch, RecipeResponse)

    async def get_all(self, filters: list[str]=[], current_user: User = Depends(azure_scheme)):
        # Fetch all objects using the crud
        objs = await self.crud.get_all()

        objs = [obj for obj in objs if (obj.is_public or obj.creator == current_user.email)]

        return self.filter_objs(objs, filters) # type: ignore


router = RecipeRouter()