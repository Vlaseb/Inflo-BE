from sqlalchemy.exc import SQLAlchemyError
from app.db.models.notifications import Notification


def get_notifications(session):
    try:
        notifications = session.query(Notification).all()
        if notifications:
            return Notification.serialize_notifications(notifications), None
        else:
            return [], "No notifications found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None


def get_notification(session, notification_id):
    try:
        notification = session.query(Notification).filter(Notification.id == notification_id).first()
        if notification:
            return notification.serialize(), None
        else:
            return None, "No notification found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None


def create_notification(session,
                        notification_id,
                        user_id,
                        type,
                        message,
                        amount,
                        sent_at
                        ):
    try:
        notification = Notification(id=notification_id,
                                    user_id=user_id,
                                    type=type,
                                    message=message,
                                    amount=amount,
                                    sent_at=sent_at
                                    )

        session.add(notification)
        return notification.serialize(), None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None