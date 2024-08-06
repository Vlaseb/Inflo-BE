import uuid
from sqlalchemy import Column, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    type = Column(String, nullable=False)
    message = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    sent_at = Column(TIMESTAMP, nullable=False)

    def serialize(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "type": str(self.type),
            "message": str(self.message),
            "amount": str(self.amount),
            "sent_at": str(self.sent_at)
        }

    @staticmethod
    def serialize_notifications(notifications):
        serialized_notifications = {}
        for notification in notifications:
            serialized_notifications[str(notification.id)] = {
                "id": str(notification.id),
                "user_id": str(notification.user_id),
                "type": str(notification.type),
                "message": str(notification.message),
                "amount": str(notification.amount),
                "sent_at": str(notification.sent_at)
        }
        return serialized_notifications
