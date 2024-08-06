import uuid
from sqlalchemy import Column, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    fees = Column(Float, nullable=True)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    to = Column(String, nullable=True)
    date = Column(TIMESTAMP, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "amount": float(self.amount),
            "fees": float(self.fees),
            "type": str(self.type),
            "name": str(self.name),
            "description": str(self.description),
            "to": str(self.to),
            "date": str(self.date)
        }

    @staticmethod
    def serialize_transactions(transactions):
        serialized_transactions = {}
        for transaction in transactions:
            serialized_transactions[str(transaction.id)] = {
                "id": str(transaction.id),
                "user_id": str(transaction.user_id),
                "amount": float(transaction.amount),
                "fees": float(transaction.fees),
                "type": str(transaction.type),
                "name": str(transaction.name),
                "description": str(transaction.description),
                "to": str(transaction.to),
                "date": str(transaction.date)
        }
        return serialized_transactions
