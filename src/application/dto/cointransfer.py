from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

class CoinTransferSchema(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    sender_id:int
    receiver_id:int
    amount:int
    create_at: datetime

class CoinTransferCreateDTO(BaseModel):
    send_id:int
    receiver_id:int
    amount:int

class CoinTransferGetDTO(BaseModel):
    user_id:int