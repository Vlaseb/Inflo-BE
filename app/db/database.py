from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

from app.core.config import USER, PASSWORD, HOST, DB_PORT, DB_NAME

Base = declarative_base()

from app.db.utils.users import *
from app.db.models.users import *

from app.db.utils.transactions import *
from app.db.models.transactions import *

from app.db.utils.budgets import *
from app.db.models.budgets import *

from app.db.utils.notifications import *
from app.db.models.notifications import *

from app.db.utils.onboarding_responses import *
from app.db.models.onboarding_responses import *

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

    # TRANSACTIONS
    @staticmethod
    def get_transactions():
        with session_scope() as session:
            return get_transactions(session)

    @staticmethod
    def get_transaction(transaction_id):
        with session_scope() as session:
            return get_transaction(session, transaction_id)

    @staticmethod
    def create_transaction(transaction_id,
                           user_id,
                           amount,
                           type,
                           name,
                           date,
                           fees=None,
                           description=None,
                           to=None):
        with session_scope() as session:
            return create_transaction(session,
                                      transaction_id,
                                      user_id,
                                      amount,
                                      type,
                                      name,
                                      date,
                                      fees,
                                      description,
                                      to)

    # BUDGETS
    @staticmethod
    def get_budgets():
        with session_scope() as session:
            return get_budgets(session)

    @staticmethod
    def get_budget(budget_id):
        with session_scope() as session:
            return get_budget(session, budget_id)

    @staticmethod
    def create_budget(budget_id,
                      user_id,
                      amount,
                      start_date,
                      end_date):
        with session_scope() as session:
            return create_budget(session,
                                 budget_id,
                                 user_id,
                                 amount,
                                 start_date,
                                 end_date)

    # NOTIFICATIONS
    @staticmethod
    def get_notifications():
        with session_scope() as session:
            return get_notifications(session)

    @staticmethod
    def get_notification(notification_id):
        with session_scope() as session:
            return get_notification(session, notification_id)

    @staticmethod
    def create_notification(notification_id,
                            user_id,
                            type,
                            message,
                            amount,
                            sent_at):
        with session_scope() as session:
            return create_notification(session,
                                       notification_id,
                                       user_id,
                                       type,
                                       message,
                                       amount,
                                       sent_at)

    # ONBOARDING_RESPONSES
    @staticmethod
    def get_responses():
        with session_scope() as session:
            return get_responses(session)

    @staticmethod
    def get_response(response_id):
        with session_scope() as session:
            return get_response(session, response_id)

    @staticmethod
    def create_response(response_id,
                        user_id,
                        question,
                        response,
                        created_at):
        with session_scope() as session:
            return create_response(session,
                                   response_id,
                                   user_id,
                                   question,
                                   response,
                                   created_at)


db = DataBase()
