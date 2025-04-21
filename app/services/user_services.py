import logging

from app.infrastructure.bd.session_to_postgres import AsyncDatabase
from app.infrastructure.repositories.user_repositorie import UserRepository
from app.infrastructure.schemas import BaseUserSchema


async def create_user_service(message):
    async with AsyncDatabase.get_session() as session:
        repo = UserRepository(session)
        new_user = BaseUserSchema(
            name=message.from_user.first_name,
            username=message.from_user.username,
            chat_id=message.chat.id,
            user_status="common_user",
        )
        user = await repo.create(new_user)
        if user:
            logging.info(f"Created new user: {user.username} ({user.chat_id})")
