from api.api import GenericRouter
from crud.recipes import recipe_crud
from models.recipe import RecipePost, RecipePatch, RecipeResponse

from fastapi import Depends
from core.openid_config import AzureScheme
from fastapi_azure_auth.user import User


class RecipeRouter(GenericRouter):
    def __init__(self) -> None:
        super().__init__(recipe_crud, RecipePost, RecipePatch, RecipeResponse)

    async def get(self, id: int, current_user: User = Depends(AzureScheme.azure_scheme)):
        obj = await self.crud.get(id)

        if obj is None:
            raise HTTPException(status_code=404, detail="Object not found")

        if not obj.is_public and obj.creator != current_user.email:
            raise HTTPException(status_code=403, detail="Forbidden")

    async def get_all(self, filters: list[str]=[], current_user: User = Depends(AzureScheme.azure_scheme)):
        print(current_user.roles)
        # Fetch all objects using the crud
        objs = await self.crud.get_all()

        objs = [obj for obj in objs if (obj.is_public)]

        return self.filter_objs(objs, filters) # type: ignore
    
    async def post(self, payload: RecipePost, current_user: User = Depends(AzureScheme.azure_scheme)):
        payload.creator = current_user.email
        return await super().post(payload)
    
    async def patch(self, id: int, payload: RecipePatch, current_user: User = Depends(AzureScheme.azure_scheme)):
        obj = await self.crud.get(id)

        if obj is None:
            raise HTTPException(status_code=404, detail="Object not found")

        if obj.creator != current_user.email:
            raise HTTPException(status_code=403, detail="Forbidden")

        return await super().patch(id, payload)
    
    async def delete(self, id: int, current_user: User = Depends(AzureScheme.azure_scheme)):
        obj = await self.crud.get(id)

        if obj is None:
            raise HTTPException(status_code=404, detail="Object not found")

        if obj.creator != current_user.email:
            raise HTTPException(status_code=403, detail="Forbidden")

        return await super().delete(id)


router = RecipeRouter()