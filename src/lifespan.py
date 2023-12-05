from contextlib import asynccontextmanager
from fastapi import FastAPI
import models
import settings


@asynccontextmanager
async def main_app_lifespan(app: FastAPI):
    """
    This context manager is responsible for setting up the database connection
    pool and tearing it down when the application is shutting down.
    """
    engine, conn = await models.create_db_engine(settings)
    app.state.engine = engine
    app.state.conn = conn
    try:
        yield
    finally:
        await app.state.conn.close()
        await app.state.engine.dispose()