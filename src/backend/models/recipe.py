from datetime import time
from pydantic import BaseModel
from typing import Optional


class Recipe(BaseModel):
    name: str
    description_short: str
    description_md: str
    creator: Optional[str] = None
    is_public: Optional[bool] = False

class RecipePost(Recipe):
    pass

class RecipeResponse(Recipe):
    id: int
    created_at: time
    updated_at: time

class RecipePatch(BaseModel):
    name: Optional[str] = None
    description_short: Optional[str] = None
    description_md: Optional[str] = None
    creator: Optional[str] = None
    is_public: Optional[bool] = False