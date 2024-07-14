from sqlalchemy.exc import SQLAlchemyError
from app.db.models.users import User


def get_users(session):
    try:
        users = session.query(User).all()
        if users:
            return User.serialize_users(users), None
        else:
            return [], "No users found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None


def get_user(session, user_id):
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            return user.serialize(), None
        else:
            return None, "No user found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None


def register_user(session, user_id, email, first_name, last_name, hashed_password=None, google_id=None):
    try:
        user = User(id=user_id,
                    email=email,
                    hashed_password=hashed_password,
                    google_id=google_id,
                    first_name=first_name,
                    last_name=last_name)

        session.add(user)
        return user.serialize(), None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None