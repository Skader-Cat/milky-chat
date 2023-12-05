import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base


async def create_db_engine(settings):
    engine = create_async_engine(
       url= settings.DatabaseSettings().GET_DB_URL,
       echo = settings.DevelopmentSettings.DEBUG,
    )

    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)

    return engine, conn

base = declarative_base()