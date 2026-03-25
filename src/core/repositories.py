from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.domain.models import (
    User,
    Merch,
    CoinTransfer,
    Purchase,
)

class AbstractUserRepository(ABC):

    @abstractmethod
    async def get_by_username(self, username: str)->Optional[User]:
        pass

    @abstractmethod
    async def create_user(self, username: str, hassed_password: str)->User:
        pass

    @abstractmethod
    async def get_by_id_with_lock(self, user_id:int)->User:
        pass

    @abstractmethod
    async def update_coins(self, user_id:int, amount: int)->None:
        pass
    
class AbstractMerhRepository(ABC):
    
    @abstractmethod
    async def get_merch_by_name(self, name:str)->Optional[Merch]:
        pass

    @abstractmethod
    async def add_purchase(self, user_id: int, merch_id: int)->None:
        pass

    @abstractmethod
    async def get_purchase(self, user_id: int)->List[Purchase]:
        pass