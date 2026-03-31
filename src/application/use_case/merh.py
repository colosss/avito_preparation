from fastapi import Depends
from src.infrastructure.database.db_helper import db_helper
from src.infrastructure.database.repositories.merch import MerchRepository

from src.core.domain.models import Merch
from src.core.repositories import AbstractMerchRepository

from src.infrastructure.database.models import Merch
from src.application.dto.merch import (
    MerchCreateDTO,
    MerchByIdDTO,
    MerchByNameDTO, 
    MerchDeleteByIdDTO,
    MerchDeleteByNameDTO,
    MerchUpdateDTO,
    MerchListDTO,
)

class CreateMerchUseCase:
    def __init__(self, merch_repo:AbstractMerchRepository)->Merch:
        self._merch_repo=merch_repo
    
    async def execute(self, merch_dto:MerchCreateDTO):
        merch=Merch(
            name=merch_dto.name,
            price=merch_dto.price
        )
        created_merch=await self._merch_repo.create_merch(merch=merch)

        return created_merch
    
class GetMerchByNameUseCase:
    def __init__(self, merch_repo: AbstractMerchRepository):
        self._merch_repo=merch_repo

    async def execute(self, merch_dto:MerchByNameDTO):
        merch_name=merch_dto.name
        merch=await self._merch_repo.get_merch_by_name(merch_name=merch_name)
        return merch

class GetMerchByIdUseCase:
    def __init__(self, merch_repo: AbstractMerchRepository):
        self._merch_repo=merch_repo

    async def execute(self, merch_dto:MerchByIdDTO):
        merch_id=merch_dto.id
        merch=await self._merch_repo.get_merch_by_id(merch_id=merch_id)

        return merch
    
class GetAllMerchUseCase:
    def __init__(self, merch_repo: AbstractMerchRepository):
        self._merch_repo=merch_repo
    
    async def execute(self, merch_dto:MerchListDTO):
        merch_list=[merch_dto.start, merch_dto.end]
        if all(merch_list):
            merchs=await self._merch_repo.get_list_merch(merch_list[0], merch_list[1])
        else:
            merchs=await self._merch_repo.get_list_merch()

        return merchs
    
class UpdateMerchUseCase:
    def __init__(self, merch_repo:AbstractMerchRepository):
        self._merch_repo=merch_repo

    async def execute(self, merch_dto:MerchUpdateDTO):
        merch=Merch(
            id=merch_dto.id,
            name=merch_dto.name,
            price=merch_dto.price
        )
        updated_merch=await self._merch_repo.update_merch(merch=merch)
        return updated_merch
    
class DeleteMercByIdhUseCase:
    def __init__(self, merch_repo:AbstractMerchRepository):
        self._merch_repo=merch_repo
    
    async def execute(self, merch_dto:MerchDeleteByIdDTO):
        merch_id=merch_dto.id
        return await self._merch_repo.delete_merch_by_id(merch_id)
    
class DeleteMerchByNameUseCase:
    def __init__(self, merch_repo:AbstractMerchRepository):
        self._merch_repo=merch_repo

    async def execute(self, merch_dto:MerchDeleteByNameDTO):
        merch_name=merch_dto.name
        return await self._merch_repo.delete_merch_by_name(merh_name=merch_name)
    
