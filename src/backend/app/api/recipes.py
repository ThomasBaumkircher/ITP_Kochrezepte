from crud.recipes import recipe_crud
from models.recipe import RecipePost, RecipePatch, RecipeResponse
from core.openid_config import azure_scheme

from fastapi import Depends, HTTPException, APIRouter
from fastapi_azure_auth.user import User


router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("/", response_model=list[RecipeResponse], response_model_exclude_unset=True)
async def get_all(current_user: User = Depends(azure_scheme)):
        # Fetch all objects using the crud
        objs = await recipe_crud.get_all()

        objs = [RecipeResponse(**vars(obj)) for obj in objs if (obj.is_public or obj.creator == current_user.email)]

        return objs

@router.post("/", response_model=RecipeResponse, status_code=201)
async def post(payload: RecipePost, current_user: User = Depends(azure_scheme)):
    payload.creator = current_user.email
    id = await recipe_crud.post(payload)
    return RecipeResponse(**vars(await recipe_crud.get(id)))

@router.get("/{id}", response_model=RecipeResponse, response_model_exclude_unset=True)
async def get(id: int, current_user: User = Depends(azure_scheme)):
    obj = await recipe_crud.get(id)

    if obj is None:
        raise HTTPException(status_code=404, detail="Object not found")

    if not obj.is_public and obj.creator != current_user.email:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    return RecipeResponse(**vars(obj))

@router.patch("/{id}", response_model=RecipeResponse, status_code=200)
async def patch(id: int, payload: RecipePatch, current_user: User = Depends(azure_scheme)):
    obj = await recipe_crud.get(id)

    if obj is None:
        raise HTTPException(status_code=404, detail="Object not found")

    if obj.creator != current_user.email:
        raise HTTPException(status_code=403, detail="Forbidden")

    return RecipeResponse(**vars(await recipe_crud.patch(id, payload)))

@router.delete("/{id}", response_model=dict, status_code=200)
async def delete(id: int, current_user: User = Depends(azure_scheme)):
    obj = await recipe_crud.get(id)

    if obj is None:
        raise HTTPException(status_code=404, detail="Object not found")

    if obj.creator != current_user.email:
        raise HTTPException(status_code=403, detail="Forbidden")

    await recipe_crud.delete(id)

    return {"detail": "Deleted"}