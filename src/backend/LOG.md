# Backend implementation log


## Quick links
- Microsoft OAuth2 package documentation: https://intility.github.io/fastapi-azure-auth/
- FastAPI settings implementation: https://intility.github.io/fastapi-azure-auth/single-tenant/fastapi_configuration/


## 2025-13-01
- [X] Implement Microsoft OAuth2 authentication

## 2025-20-01
- [X] Implement generic CRUD and API interfaces
- [X] Discuss database schema
- [X] Implement database schema

## 2025-27-01
- [X] Research further on Microsoft OAuth2
- [X] Implement schemas for API endpoints
- [X] Modify generic API interface to use schemas (POST, PATCH)

## 2025-03-02
- [X] Look for bugs and fix
- Bugs:
    - [X] Patch changing ID
    - [X] Get all recipes returning private recipes from other users
    - [X] Include redirect URI in OAuth2 configuration
- [X] Implement user recipes endpoint

## 2025-10-02
- [ ] Finish Microsoft OAuth2 implementation in frontend
    - Problem: The frontend does not support ssl yet and no workaround has been found

## 2025-24-02
- [ ] Implement backend route tests
    - Problem: Monkeypatch package is broken and cannot be installed
- [X] Finish Microsoft OAuth2 implementation in frontend

## 2025-03-03
- [ ] Implement backend route tests
    - Wait for fix on monkeypatch install
- [ ] Help Julian with frontend implementation