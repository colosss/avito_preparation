from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from src.infrastructure.database.models import User
from src.core.repositories import AbstractUserRepository
from typing import List, Optional
import asyncio
import logging


class UserRepository(AbstractUserRepository):
    def __init__(self, session:AsyncSession):
        self.session=session

    async def get_by_id(self, user_id:int)->Optional[User]:
        user=await self.session.get(User, user_id)
        return user