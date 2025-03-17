import pytest
from starlette.testclient import TestClient
from fastapi_azure_auth.user import User

from app import app
from core.openid_config import azure_scheme


async def mock_user():
    test_user = User(email="asdf", roles=["user"], aud="asdf", iss="asdf", iat=1, nbf=1, exp=1, azp="asdf", sub="asdf", ver="2.0", claims={}, access_token="asdf")
    yield test_user

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here

@pytest.fixture(scope="module")
def test_app_mock_auth():
    app.dependency_overrides[azure_scheme] = mock_user
    client = TestClient(app)
    yield client  # testing happens here