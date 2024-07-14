from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

from app.core.config import USER, PASSWORD, HOST, DB_PORT, DB_NAME

Base = declarative_base()

from app.db.utils.users import *
from app.db.models.users import *

engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{DB_PORT}/{DB_NAME}')

Base.metadata.create_all(bind=engine)


@contextmanager
def session_scope():
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class DataBase:

    # AUTH
    @staticmethod
    def get_users():
        with session_scope() as session:
            return get_users(session)

    @staticmethod
    def get_user(user_id):
        with session_scope() as session:
            return get_user(session, user_id)

    @staticmethod
    def register_user(user_id, email, first_name, last_name, hashed_password=None, google_id=None):
        with session_scope() as session:
            return register_user(session, user_id, email, first_name, last_name, hashed_password, google_id)


db = DataBase()
