import json
from fastapi import status

from models.recipe import RecipePost, RecipePatch, RecipeResponse
from database.model import Recipe
from crud.recipes import RecipeCRUD


def test_get_all_unauthorized(test_app):
    response = test_app.get("/api/recipes")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_get_one_unauthorized(test_app):
    response = test_app.get("/api/recipes/1")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_create_unauthorized(test_app):
    response = test_app.post("/api/recipes", json={})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_update_unauthorized(test_app):
    response = test_app.patch("/api/recipes/1", json={})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_delete_unauthorized(test_app):
    response = test_app.delete("/api/recipes/1")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    

def test_get_all(test_app_mock_auth, monkeypatch):
    recipe = Recipe(id=1, name="test", creator="asdf", is_public=True, created_at="2021-01-01T00:00:00Z", updated_at="2021-01-01T00:00:00Z", description_short="short", description_md="md")
    async def mock_get_all(*_):
        return [recipe]
    monkeypatch.setattr(RecipeCRUD, "get_all", mock_get_all)

    response = test_app_mock_auth.get("/api/recipes")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [RecipeResponse(**vars(recipe)).model_dump()]

def test_get_one(test_app_mock_auth, monkeypatch):
    recipe = Recipe(id=1, name="test", creator="asdf", is_public=True, created_at="2021-01-01T00:00:00Z", updated_at="2021-01-01T00:00:00Z", description_short="short", description_md="md")
    async def mock_get(*_):
        return recipe
    monkeypatch.setattr(RecipeCRUD, "get", mock_get)

    response = test_app_mock_auth.get("/api/recipes/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == RecipeResponse(**vars(recipe)).model_dump()

def test_create(test_app_mock_auth, monkeypatch):
    recipe = Recipe(name="test", is_public=True, description_short="short", description_md="md")
    async def mock_create(*_):
        return 1
    monkeypatch.setattr(RecipeCRUD, "post", mock_create)

    recipe = Recipe(id=1, name="test", creator="asdf", is_public=True, created_at="2021-01-01T00:00:00Z", updated_at="2021-01-01T00:00:00Z", description_short="short", description_md="md")
    async def mock_get(*_):
        return recipe
    monkeypatch.setattr(RecipeCRUD, "get", mock_get)

    response = test_app_mock_auth.post("/api/recipes", json=RecipePost(**vars(recipe)).model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == RecipeResponse(**vars(recipe)).model_dump()

def test_update(test_app_mock_auth, monkeypatch):
    recipe = Recipe(id=1, name="test", creator="asdf", is_public=True, created_at="2021-01-01T00:00:00Z", updated_at="2021-01-01T00:00:00Z", description_short="short", description_md="md")
    async def mock_get(*_):
        return recipe
    monkeypatch.setattr(RecipeCRUD, "get", mock_get)

    async def mock_update(*_):
        return recipe
    monkeypatch.setattr(RecipeCRUD, "patch", mock_update)
    
    response = test_app_mock_auth.patch("/api/recipes/1", json=RecipePatch(**vars(recipe)).model_dump())
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == RecipeResponse(**vars(recipe)).model_dump()

def test_delete(test_app_mock_auth, monkeypatch):
    recipe = Recipe(id=1, name="test", creator="asdf", is_public=True, created_at="2021-01-01T00:00:00Z", updated_at="2021-01-01T00:00:00Z")
    async def mock_get(*_):
        return recipe
    monkeypatch.setattr(RecipeCRUD, "get", mock_get)

    async def mock_delete(*_):
        return 1
    monkeypatch.setattr(RecipeCRUD, "delete", mock_delete)

    response = test_app_mock_auth.delete("/api/recipes/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"detail": "Deleted"}


def test_patch_wrong_user(test_app_mock_auth, monkeypatch):
    recipe = Recipe(id=1, name="test", creator="test", is_public=True, created_at="2021-01-01T00:00:00Z", updated_at="2021-01-01T00:00:00Z")
    async def mock_get(*_):
        return recipe
    monkeypatch.setattr(RecipeCRUD, "get", mock_get)

    response = test_app_mock_auth.patch("/api/recipes/1", json={"name": "new name"})
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {"detail": "Forbidden"}

def test_delete_wrong_user(test_app_mock_auth, monkeypatch):
    recipe = Recipe(id=1, name="test", creator="test", is_public=True, created_at="2021-01-01T00:00:00Z", updated_at="2021-01-01T00:00:00Z")
    async def mock_get(*_):
        return recipe
    monkeypatch.setattr(RecipeCRUD, "get", mock_get)

    response = test_app_mock_auth.delete("/api/recipes/1")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {"detail": "Forbidden"}


def test_get_not_found(test_app_mock_auth, monkeypatch):
    async def mock_get(*_):
        return None
    monkeypatch.setattr(RecipeCRUD, "get", mock_get)

    response = test_app_mock_auth.get("/api/recipes/1")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Object not found"}

def test_patch_not_found(test_app, monkeypatch):
    async def mock_get(*_):
        return None
    monkeypatch.setattr(RecipeCRUD, "get", mock_get)

    response = test_app.patch("/api/recipes/1", json={})

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Object not found"}

def test_delete_not_found(test_app, monkeypatch):
    async def mock_get(*_):
        return None
    monkeypatch.setattr(RecipeCRUD, "get", mock_get)

    response = test_app.delete("/api/recipes/1")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Object not found"}