import logging
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.infrastructure.bd.models import User
from app.infrastructure.schemas import BaseUserSchema


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_chat_id(self, chat_id: int) -> User | None:
        try:
            result = await self.session.execute(
                select(User).where(User.chat_id == chat_id)
            )
            return result.scalars().first()
        except Exception as e:
            logging.exception(f"Failed to get user by chat_id {chat_id}: {e}")
            await self.session.rollback()
            return None

    async def create(self, user_data: BaseUserSchema) -> User | None:
        try:
            existing_user = await self.get_by_chat_id(user_data.chat_id)
            if existing_user:
                logging.warning(f"User with chat_id {user_data.chat_id} already exists")
                return None

            new_user = User(
                name=user_data.name,
                username=user_data.username,
                chat_id=user_data.chat_id,
                user_status=user_data.user_status,
                created_at=datetime.now(),
                last_seen=datetime.now(),
            )
            self.session.add(new_user)
            await self.session.commit()
            await self.session.refresh(new_user)
            return new_user
        except Exception as e:
            logging.exception(f"Failed to create user: {e}")
            await self.session.rollback()
            return None

    async def delete(self, chat_id: int) -> None:
        try:
            user = await self.get_by_chat_id(chat_id)
            if user:
                await self.session.delete(user)
                await self.session.commit()
            else:
                logging.error(f"User with chat_id:{chat_id} not found")
        except Exception as e:
            logging.info(e)
            await self.session.rollback()
