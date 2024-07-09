from sqlalchemy.exc import SQLAlchemyError
from app.db.models.users import User


def get_users(session):
    try:
        users = session.query(User).all()
        if users:
            return User.serialize_users(users), None
        else:
            return None, "No users found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None
