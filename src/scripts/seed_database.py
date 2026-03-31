import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.database.models import Merch
from src.infrastructure.database.db_helper import db_helper
from sqlalchemy import select

MERCH_DATA=[
    {"name":"t-shirt", "price": 80},
    {"name":"cup", "price": 20},
    {"name":"book", "price": 50},
    {"name":"pen", "price": 10},
    {"name":"powerbank", "price": 200},
    {"name":"hoody", "price": 300},
    {"name":"umbrella", "price": 200},
    {"name":"socks", "price": 10},
    {"name":"wallet", "price": 50},
    {"name":"pink-hoody", "price": 500},
]


async def seed_merch():
    async with db_helper.session_factory() as session:
        async with session.begin():
            result = await session.execute(select(Merch))
            existing_merch=result.scalars().all()

            if existing_merch:
                print("База уже заполнена мерчем")
                return
            
            print("Заполнение базы...")
            for item in MERCH_DATA:
                merch=Merch(name=item["name"], price=item["price"])
                session.add(merch)

            await session.commit()
            print("Готово!")

if __name__=="__main__":
    asyncio.run(seed_merch())