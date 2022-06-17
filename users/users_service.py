import re
from sqlite3 import Cursor
from typing import List

from sqlalchemy import select
from sqlalchemy.sql import text

import bcrypt
from sqlalchemy.orm import Session, sessionmaker

from database.database import engine, get_database
from database.users_model import User

engine = get_database()
Session = sessionmaker(bind=engine)
session = Session()
LOGIN_RE = r'^[a-zA-Z0-9]+$'


def validate_login(login: str):
    if not len(login) > 3:
        return False

    return re.match(LOGIN_RE, login) is not None


def validate_password(password):
    return len(password) > 4


# def has_user(engine, login: str):
#     return len(db.execute("SELECT * FROM users WHERE login = ?", (login,)).fetchall()) > 0

def has_user(login_to_be_found: str):
    # user = session.query(User).filter(User.login == login_to_be_found).count() > 0
    return 0


def login(user_login: str, password: str):
    # user = db.execute("SELECT * FROM users WHERE login = ?", (login,)).fetchone()
    user = select(login).where(login == user_login)
    if user is None:
        return None

    if not bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
        return None

    return User(id=user[0], login=user[1])


# def create_user(db: Cursor, login: str, password):
#     salt = bcrypt.gensalt()
#     password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
#
#     db.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login.lower(), password))


def get_all_users(db: Cursor) -> List[User]:
    return [User(id=user[0], login=user[1]) for user in db.execute("SELECT * FROM users")]


def remove_user(db: Cursor, login):
    db.execute("DELETE FROM users WHERE login = ?", (login,))


def create_user(login: str, password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    new_user = User(login=login, password=hashed_password)
    session.add(new_user)
    session.commit()
