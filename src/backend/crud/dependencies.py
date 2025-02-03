from typing import Generator

from database.config import session
from crud.recipes import recipe_crud


def get_db() -> Generator:
    with session.begin():
        yield session


def get_recipe_crud() -> Generator:
    yield recipe_crud