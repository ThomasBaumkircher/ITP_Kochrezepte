from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


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
    created_at: datetime
    updated_at: datetime

class RecipeList(BaseModel):
    count: int
    recipes: List[RecipeResponse]

class RecipePatch(BaseModel):
    id: int
    name: Optional[str] = None
    description_short: Optional[str] = None
    description_md: Optional[str] = None
    creator: Optional[str] = None
    is_public: Optional[bool] = False