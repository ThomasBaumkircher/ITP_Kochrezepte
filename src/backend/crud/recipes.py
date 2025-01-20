from crud.crud import GenericCRUD
from database.model import Recipe


class RecipeCRUD(GenericCRUD[Recipe]):
    def __init__(self) -> None:
        super().__init__(Recipe)


recipe_crud = RecipeCRUD()