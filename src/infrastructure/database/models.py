from sqlalchemy.orm import Mapped, mapped_column
from src.infrastructure.database.base import Base
from sqlalchemy import String, Integer, ForeignKey, BigInteger, DateTime, func

class User(Base):
    __tablename__ = "user"

    user_name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    coins: Mapped[int] = mapped_column(Integer, default=1000)

class Merch(Base):
    __tablename__ = "merch"

    name: Mapped[str] = mapped_column(String(100), unique=True)
    price: Mapped[str] = mapped_column(Integer)

class CoinTransfer(Base):
    sender_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    receiver_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    amount: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

class Purchase(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    merch_id: Mapped[int] = mapped_column(ForeignKey("merch.id"))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())