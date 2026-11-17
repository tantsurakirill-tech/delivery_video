import decimal

from sqlalchemy import Column, String, Numeric, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Parcel(Base):
    __tablename__ = 'parcels'

    # __table_args__ = {
    #     'schema': 'parcels'
    # } Если схема не публичная

    # id = Column(Integer, primary_key=True)

    id: Mapped[int] = mapped_column(primary_key=True)
    tracking_code: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    recipient: Mapped[str] = mapped_column(String(100), nullable=False)
    weight_kg: Mapped[decimal.Decimal] = mapped_column(Numeric(6,2), nullable=False)
    status: Mapped[str] = mapped_column(String(20), server_default=text("created"), nullable=False)

    def __str__(self) -> str:
        return f"{self.tracking_code} {self.recipient} {self.status}"

    def __repr__(self) -> str:
        return f"Parcel(tracking_code={self.tracking_code}, recipient={self.recipient}, status={self.status})"