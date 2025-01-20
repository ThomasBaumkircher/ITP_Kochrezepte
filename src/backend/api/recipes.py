from api.api import GenericRouter
from crud.recipes import recipe_crud
from models.recipe import RecipePost, RecipePatch, RecipeResponse


class RecipeRouter(GenericRouter):
    def __init__(self) -> None:
        super().__init__(recipe_crud, RecipePost, RecipePatch, RecipeResponse)


router = RecipeRouter()