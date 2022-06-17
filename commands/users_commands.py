from sqlalchemy.orm import sessionmaker
from database.users_model import User
from users import users_service
from database.database import engine


class RegisterException(Exception):
    pass


class WrongDataException(RegisterException):
    pass


class UserExistsException(RegisterException):
    pass


def register(login, password):
    if not users_service.validate_login(login):
        raise WrongDataException("Wrong login")

    if not users_service.validate_password(password):
        raise WrongDataException("Wrong password")

    if users_service.has_user(login):
        raise UserExistsException("User exists")

    else:
        users_service.create_user(login, password)


def login(login, password) -> User:
    return users_service.login(login, password)
