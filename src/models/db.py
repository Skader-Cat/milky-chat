import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker

AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=None,
    expire_on_commit=False,
    class_=AsyncSession
)

async def create_db_engine(settings):
    engine = create_async_engine(
       url= settings.DatabaseSettings().GET_DB_URL,
       echo = settings.DevelopmentSettings.DEBUG,
    )

    AsyncSessionLocal.configure(bind=engine)

    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)

    return engine, conn

base = declarative_base()

