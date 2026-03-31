from abc import ABC, abstractmethod
from typing import List, Optional, Sequence
from src.core.domain.models import (
    User,
    Merch,
    CoinTransfer,
    Purchase,
)

class AbstractUserRepository(ABC):

    @abstractmethod
    async def get_by_id(self, id:int)->Optional[User]:
        pass

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
    async def update_coins(self, user_id:int, coins: int)->None:
        pass
    
    @abstractmethod
    async def update_username(self, user_id:int, username:str)->Optional[User]:
        pass

    @abstractmethod
    async def update_user_password(self, user_id:int, hashed_password:str)->Optional[User]:
        pass

    @abstractmethod
    async def delete_user_by_id(self, user_id:int)->None:
        pass


class AbstractMerchRepository(ABC):

    @abstractmethod
    async def create_merch(self, merch: Merch)->Merch:
        pass
    
    @abstractmethod
    async def get_merch_by_name(self, name:str)->Optional[Merch]:
        pass

    @abstractmethod
    async def get_merch_by_id(self, merch_id:int)->Optional[Merch]:
        pass

    @abstractmethod
    async def get_list_merch(self, start:Optional[int], end:Optional[int])->Sequence[Merch]:
        pass

    @abstractmethod
    async def update_merch(self, merch:Merch)->Merch:
        pass

    @abstractmethod
    async def delete_merch_by_id(self, merch_id:int)->None:
        pass

    @abstractmethod
    async def delete_merch_by_name(self, merh_name:str)->None:
        pass

class AbstractPurchaseRepository(ABC):

    @abstractmethod
    async def add_purchase(self, user_id: int, merch_id: int)->None:
        pass

    @abstractmethod
    async def get_purchase(self, user_id: int)->Sequence[Purchase]:
        pass

class AbstractCoinTransferRepository(ABC):

    @abstractmethod
    async def create_transfer(self, send_id: int, receiver_id: int, amount: int)->CoinTransfer:
        pass

    @abstractmethod
    async def get_transfers_received(self, user_id: int)->Sequence[CoinTransfer]:
        pass

    @abstractmethod
    async def get_transfers_sent(self, user_id: int)->Sequence[CoinTransfer]:
        pass 