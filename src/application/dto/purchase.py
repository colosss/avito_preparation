from pydantic import BaseModel, ConfigDict
from datetime import datetime

class PurchaseSchema(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    user_id:int
    merch_id:int
    create_at:datetime

class PurchaseAddDTO(BaseModel):
    user_id:int
    merch_id:int

class PurchaseGetDTO(BaseModel):
    user_id:int