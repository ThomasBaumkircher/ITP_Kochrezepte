from typing import Generator

from database.config import async_session


async def get_db() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield session
