from app.db.database import db


def get_users():
    return db.get_users()
