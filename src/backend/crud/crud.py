from fastapi import HTTPException
from database.config import session
from sqlalchemy import ScalarResult, select
from typing import Type, TypeVar, Generic
from datetime import datetime

# Model Type
T = TypeVar('T')


# universal crud operations
class GenericCRUD(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    async def post(self, payload) -> int:
        obj = self.model(**vars(payload))

        obj.created_at = datetime.now()
        obj.updated_at = datetime.now()

        session.add(obj)
        session.commit()

        return obj.id # type: ignore

    async def patch(self, id: int, payload) -> T:
        data = payload.model_dump()
        obj = session.get(self.model, id)

        if not obj:
            raise HTTPException(status_code=404, detail="Not found")

        # Update the object with the new data
        for key, value in data.items():
            setattr(obj, key, value)

        obj.updated_at = datetime.now()

        session.commit()
        return obj

    async def get_all(self) -> ScalarResult[T]:
        stmt = select(self.model).where(self.model.deleted_at == None)
        res = session.execute(stmt)
        objs = res.scalars()

        return objs

    async def get(self, id: int) -> T:
        stmt = select(self.model).where(self.model.id == id).where(self.model.deleted_at == None) # type: ignore
        res = session.execute(stmt)
        obj = res.scalar()

        if not obj:
            raise HTTPException(status_code=404, detail="Not found")

        return obj

    async def delete(self, id: int) -> int:
        stmt = select(self.model).where(self.model.id == id).where(self.model.deleted_at == None) # type: ignore
        res = session.execute(stmt)
        obj = res.scalar()

        if not obj:
            raise HTTPException(status_code=404, detail="Not found")
        
        obj.deleted_at = datetime.now()
        obj.updated_at = datetime.now()

        return id
