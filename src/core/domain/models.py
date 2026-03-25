from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    username: str
    hashed_password: str
    coins: int

@dataclass
class Merch:
    id: int
    name: str
    price: int

@dataclass
class CoinTransfer:
    id: int
    sender_id: int
    receiver_id: int
    amount: int
    created_at: datetime

@dataclass
class Purchase:
    id: int
    user_id: int
    merch_id: int
    created_at: datetime