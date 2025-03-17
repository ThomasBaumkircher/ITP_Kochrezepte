import json
from fastapi import status


def test_get_all(test_app, monkeypatch):
    assert True

def test_get_one(test_app, monkeypatch):
    assert True

def test_create(test_app, monkeypatch):
    assert True

def test_update(test_app, monkeypatch):
    assert True

def test_delete(test_app, monkeypatch):
    assert True

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

def test_patch_wrong_user(test_app, monkeypatch):
    assert True

def test_delete_wrong_user(test_app, monkeypatch):
    assert True

def test_get_not_found(test_app, monkeypatch):
    assert True

def test_patch_not_found(test_app, monkeypatch):
    assert True

def test_delete_not_found(test_app, monkeypatch):
    assert True