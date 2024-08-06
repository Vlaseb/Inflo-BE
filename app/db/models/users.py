import uuid
from sqlalchemy import Column, String, Float, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    email = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=True)
    google_id = Column(String, nullable=True)
    balance = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "email": str(self.email),
            "first_name": str(self.first_name),
            "last_name": str(self.last_name),
            "hashed_password": str(self.hashed_password),
            "google_id": str(self.google_id),
            "balance": float(self.balance),
            "created_at": str(self.created_at)
        }

    @staticmethod
    def serialize_users(users):
        serialized_users = {}
        for user in users:
            serialized_users[str(user.id)] = {
                "id": str(user.id),
                "email": str(user.email),
                "first_name": str(user.first_name),
                "last_name": str(user.last_name),
                "hashed_password": str(user.hashed_password),
                "google_id": str(user.google_id),
                "balance": float(user.balance),
                "created_at": str(user.created_at)
        }
        return serialized_users
