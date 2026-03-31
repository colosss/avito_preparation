from pydantic import BaseModel, ConfigDict
from typing import Optional

class MerchSchema(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    name:str
    price:int

class MerchCreateDTO(BaseModel):
    name:str
    price:int

class MerchUpdateDTO(BaseModel):
    id:int
    name:Optional[str]=None
    price:Optional[int]=None

class MerchByIdDTO(BaseModel):
    id:int

class MerchByNameDTO(BaseModel):
    name:str

class MerchListDTO(BaseModel):
    start:Optional[int]=None
    end:Optional[int]=None

class MerchDeleteByIdDTO(BaseModel):
    id:int

class MerchDeleteByNameDTO(BaseModel):
    name:str

