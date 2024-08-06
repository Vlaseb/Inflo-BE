import uuid
from sqlalchemy import Column, Float, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    start_date = Column(TIMESTAMP, nullable=False)
    end_date = Column(TIMESTAMP, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "amount": str(self.amount),
            "start_date": str(self.start_date),
            "end_date": str(self.end_date)
        }

    @staticmethod
    def serialize_budgets(budgets):
        serialized_budgets = {}
        for budget in budgets:
            serialized_budgets[str(budget.id)] = {
                "id": str(budget.id),
                "user_id": str(budget.user_id),
                "amount": str(budget.amount),
                "start_date": str(budget.start_date),
                "end_date": str(budget.end_date)
        }
        return serialized_budgets
