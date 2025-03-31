from pydantic import BaseModel
from typing import Optional


class Recipe(BaseModel):
    name: str
    description_short: str
    description_md: str
    is_public: Optional[bool] = False

class RecipePost(Recipe):
    pass

class RecipeResponse(BaseModel):
    id: int
    created_at: str
    updated_at: str

class RecipePatch(BaseModel):
    name: Optional[str] = None
    description_short: Optional[str] = None
    description_md: Optional[str] = None
    is_public: Optional[bool] = False