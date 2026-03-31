from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from src.infrastructure.database.models import Merch
from src.core.repositories import AbstractMerchRepository
from typing import List, Optional
import asyncio
import logging

class MerchRepository(AbstractMerchRepository):
    def __init__(self, session:AsyncSession):
        self.session=session

    async def get_merch_by_id(self, merch_id:int)->Optional[Merch]:
        merch=await self.session.get(Merch, merch_id)
        return merch

    async def get_merch_by_name(self, name:str)->Optional[Merch]:
        merch=await self.session.get(Merch, name)
        return merch

    async def get_list_merch(self, start:Optional[int]=None, end:Optional[int]=None)->List[Merch]:
        stmt=select(Merch)
        if start is not None:
            stmt = stmt.offset(start)
            if end is not None:
                stmt = stmt.limit(end-start)
        result=await self.session.execute(stmt)
        merch=result.scalar().all()
        return list(merch)

    async def create_merch(self, merh: Merch)->Merch:
        self.session.add(merh)
        await self.session.commit()
        await self.session.refresh(merh)
        return merh
    
    async def update_merch(self, merch:Merch)->Merch:
        db_merch=await self.get_merch_by_id(merch_id=merch.id)

        if db_merch:
            db_merch.name=merch.name
            db_merch.price=merch.price
            
            await self.session.commit()
            await self.session.refresh(db_merch)
        return db_merch
    
    async def delete_merch_by_id(self, merch_id:int)->None:
        merch=await self.get_merch_by_id(merch_id=merch_id)
        if merch:
            await self.session.delete(merch)
            await self.session.commit()
        return
    
    async def delete_merch_by_name(self, merh_name:str)->None:
        merch=await self.get_merch_by_name(merh_name=merh_name)
        if merch:
            await self.session.delete(merch)
            await self.session.commit()
        return