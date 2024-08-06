import uuid
from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Onboarding_response(Base):
    __tablename__ = "onboarding_responses"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    question = Column(String, nullable=False)
    response = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "question": str(self.question),
            "response": str(self.response),
            "created_at": str(self.created_at)
        }

    @staticmethod
    def serialize_responses(responses):
        serialized_responses = {}
        for response in responses:
            serialized_responses[str(response.id)] = {
                "id": str(response.id),
                "user_id": str(response.user_id),
                "question": str(response.question),
                "response": str(response.response),
                "created_at": str(response.created_at)
        }
        return serialized_responses
