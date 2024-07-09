import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    email = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "email": str(self.email),
            "first_name": str(self.first_name),
            "last_name": str(self.last_name),
            "hashed_password": str(self.hashed_password),
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
        }
        return serialized_users
