from sqlalchemy.exc import SQLAlchemyError
from app.db.models.onboarding_responses import Onboarding_response


def get_responses(session):
    try:
        responses = session.query(Onboarding_response).all()
        if responses:
            return Onboarding_response.serialize_budgets(responses), None
        else:
            return [], "No responses found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None


def get_response(session, response_id):
    try:
        response = session.query(Onboarding_response).filter(Onboarding_response.id == response_id).first()
        if response:
            return response.serialize(), None
        else:
            return None, "No response found"
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None


def create_response(session,
                    response_id,
                    user_id,
                    question,
                    response,
                    created_at
                    ):
    try:
        response = Onboarding_response(id=response_id,
                                       user_id=user_id,
                                       question=question,
                                       response=response,
                                       created_at=created_at
                                       )

        session.add(response)
        return response.serialize(), None
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return error, None