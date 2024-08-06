from sqlalchemy.exc import SQLAlchemyError
from app.db.models.budgets import Budget


def get_budgets(session):
    try:
        budgets = session.query(Budget).all()
        if budgets:
            return Budget.serialize_budgets(budgets), None
        else:
            return [], "No budgets found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None


def get_budget(session, budget_id):
    try:
        budget = session.query(Budget).filter(Budget.id == budget_id).first()
        if budget:
            return budget.serialize(), None
        else:
            return None, "No budget found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None


def create_budget(session,
                  budget_id,
                  user_id,
                  amount,
                  start_date,
                  end_date
                  ):
    try:
        budget = Budget(id=budget_id,
                        user_id=user_id,
                        amount=amount,
                        start_date=start_date,
                        end_date=end_date
                        )

        session.add(budget)
        return budget.serialize(), None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None