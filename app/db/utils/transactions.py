from sqlalchemy.exc import SQLAlchemyError
from app.db.models.transactions import Transaction


def get_transactions(session):
    try:
        transactions = session.query(Transaction).all()
        if transactions:
            return Transaction.serialize_transactions(transactions), None
        else:
            return [], "No transactions found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None


def get_transaction(session, transaction_id):
    try:
        transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
        if transaction:
            return transaction.serialize(), None
        else:
            return None, "No transaction found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None


def create_transaction(session,
                       transaction_id,
                       user_id,
                       amount,
                       type,
                       name,
                       date,
                       fees=None,
                       description=None,
                       to=None,
                       ):
    try:
        transaction = Transaction(id=transaction_id,
                                  user_id=user_id,
                                  amount=amount,
                                  type=type,
                                  name=name,
                                  date=date,
                                  fees=fees,
                                  description=description,
                                  to=to,
                                  )

        session.add(transaction)
        return transaction.serialize(), None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None