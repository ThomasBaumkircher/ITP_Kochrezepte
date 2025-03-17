from api.api import GenericRouter
from crud.recipes import recipe_crud
from models.recipe import RecipePost, RecipePatch, RecipeResponse
from core.openid_config import azure_scheme

from fastapi import Depends, HTTPException
from fastapi_azure_auth.user import User


class RecipeRouter(GenericRouter):
    def __init__(self) -> None:
        super().__init__(recipe_crud, RecipePost, RecipePatch, RecipeResponse)

        self.add_api_route("/", self.get_all, response_model=list[RecipeResponse], response_model_exclude_unset=True, methods=["GET"])
        self.add_api_route("/", self.post, response_model=RecipeResponse, status_code=201, methods=["POST"])
        self.add_api_route("/{id}", self.get, response_model=RecipeResponse, response_model_exclude_unset=True, methods=["GET"])
        self.add_api_route("/{id}", self.patch, response_model=RecipeResponse, status_code=200, response_model_exclude_unset=True, methods=["PATCH"])
        self.add_api_route("/{id}", self.delete, response_model=dict, status_code=200, methods=["DELETE"])

    async def get(self, id: int, current_user: User = Depends(azure_scheme)):
        obj = await self.crud.get(id)

        if obj is None:
            raise HTTPException(status_code=404, detail="Object not found")

        if not obj.is_public and obj.creator != current_user.email:
            raise HTTPException(status_code=403, detail="Forbidden")
        
        return self.response_model(**vars(await super().get(id)))

    async def get_all(self, filters: list[str]=[], current_user: User = Depends(azure_scheme)):
        # Fetch all objects using the crud
        objs = await self.crud.get_all()

        objs = [self.response_model(**vars(obj)) for obj in objs if (obj.is_public or obj.creator == current_user.email)]

        return self.filter_objs(objs, filters) # type: ignore
    
    async def post(self, payload: RecipePost, current_user: User = Depends(azure_scheme)):
        payload.creator = current_user.email
        return await super().post(payload)
    
    async def patch(self, id: int, payload: RecipePatch, current_user: User = Depends(azure_scheme)):
        obj = await self.crud.get(id)

        if obj is None:
            raise HTTPException(status_code=404, detail="Object not found")

        if obj.creator != current_user.email:
            raise HTTPException(status_code=403, detail="Forbidden")

        return self.response_model(**vars(await super().patch(id, payload)))
    
    async def delete(self, id: int, current_user: User = Depends(azure_scheme)):
        obj = await self.crud.get(id)

        if obj is None:
            raise HTTPException(status_code=404, detail="Object not found")

        if obj.creator != current_user.email:
            raise HTTPException(status_code=403, detail="Forbidden")

        return await super().delete(id)


router = RecipeRouter()