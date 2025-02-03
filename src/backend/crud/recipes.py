from crud.crud import GenericCRUD
from database.model import Recipe


class RecipeCRUD(GenericCRUD[Recipe]):
    def __init__(self) -> None:
        super().__init__(Recipe)
    
    async def get_user_recipes(self, user_id: str):
        return self.model.query.filter(self.model.creator == user_id).all()


recipe_crud = RecipeCRUD()