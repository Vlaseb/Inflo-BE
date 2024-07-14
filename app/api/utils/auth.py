import uuid
from app.db.database import db
from app.core.security import AuthHandler

auth_handler = AuthHandler()


def login(user_data):
    login_data = user_data.model_dump()
    users_data, _ = db.get_users()

    for key in users_data:
        if users_data[key].get("email") == login_data.get("email"):
            user_data = users_data[key]

            if auth_handler.verify_password(login_data.get("password"), user_data.get("hashed_password")):
                login_data["email"] = user_data.get("email")
                login_data["id"] = user_data.get("id")
                login_data["first_name"] = user_data.get("first_name")
                login_data["last_name"] = user_data.get("last_name")

                return login_data, None
            else:
                return login_data, "Incorrect password"
    return login_data, "Incorrect email"


def login_google(user_data):
    login_data = user_data.model_dump()
    users_data, _ = db.get_users()

    for key in users_data:
        if users_data[key].get("email") == login_data.get("email"):
            user_data = users_data[key]

            if user_data.get("google_id") == login_data.get("google_id"):
                login_data["email"] = user_data.get("email")
                login_data["id"] = user_data.get("id")
                login_data["first_name"] = user_data.get("first_name")
                login_data["last_name"] = user_data.get("last_name")

                return login_data, None
            else:
                return None, "Could not validate credentials"

    # If email is not found then register an account
    new_user_id = str(uuid.uuid4())

    db.register_user(user_id=new_user_id,
                     first_name=login_data.get("first_name"),
                     last_name=login_data.get("last_name"),
                     google_id=login_data.get("google_id"),
                     email=login_data.get("email"))

    login_data["id"] = new_user_id
    return login_data, None


def register(user_data):
    register_data = user_data.model_dump()
    users_data, _ = db.get_users()

    for key in users_data:
        if users_data[key].get("email") == register_data.get("email"):
            return None, "Email already registered"

    hashed_password = auth_handler.get_password_hash(register_data.get("password"))
    new_user_id = str(uuid.uuid4())

    db.register_user(user_id=new_user_id,
                     first_name=register_data.get("first_name"),
                     last_name=register_data.get("last_name"),
                     email=register_data.get("email"),
                     hashed_password=hashed_password)

    register_data["id"] = new_user_id
    return register_data, None


def token_refresh(refresh_token):
    access_token, user_id = auth_handler.refresh_token(refresh_token)
    user_data, error = db.get_user(user_id)
    user_data["access_token"] = access_token

    if error:
        return None, "Could not validate credentials"

    return user_data, None
