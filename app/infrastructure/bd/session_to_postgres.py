import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core import config_settings

logger = logging.getLogger(__name__)


class AsyncDatabase:
    _engine = None
    _session_factory: sessionmaker = None

    @classmethod
    def init_engine(cls):
        if not cls._engine:
            logger.info("Initializing async database engine...")
            cls._engine = create_async_engine(
                config_settings.async_db_url,
                echo=False,
                future=True,
            )
            cls._session_factory = sessionmaker(
                bind=cls._engine,
                class_=AsyncSession,
                expire_on_commit=False,
            )
            logger.info("Async engine initialized.")

    @classmethod
    def get_session(cls) -> AsyncSession:
        if not cls._session_factory:
            raise RuntimeError("Database engine not initialized. Call init_engine() first.")
        return cls._session_factory()

    @staticmethod
    async def save(session: AsyncSession, instance):
        logger.debug(f"Saving: {instance}")
        session.add(instance)
        await session.commit()
        await session.refresh(instance)
        logger.debug(f"Saved and refreshed: {instance}")
        return instance

    @staticmethod
    async def delete(session: AsyncSession, instance):
        logger.debug(f"Deleting: {instance}")
        await session.delete(instance)
        await session.commit()
        logger.debug("Deleted.")
