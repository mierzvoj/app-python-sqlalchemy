import os
import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from database import users_model, rooms_model

db_path = os.path.join(
    os.path.dirname(
        os.path.abspath(__name__)
    ), "db.sqlite")

engine = None
Session = sessionmaker(bind=engine)


def get_database():
    # global db
    # if db is None:
    #     print(db_path)
    #     db = sqlite3.connect(db_path)
    #     db.execute("PRAGMA foreign_keys = ON;")
    # return db
    global engine
    if engine is None:
        print("db_path: ", db_path)
        engine = create_engine("sqlite:///" + db_path, echo=True, future=True)
    return engine


def initialize(db):
    print("Initialising db: ", db)
    users_model.init_model(db)
    rooms_model.init_model(db)
    # users_model.Base.metadata.create_all(db)
    # rooms_model.Base.metadata.create_all(db)
    # print("Dropping db")
    # db.isolation_level = None
    # for call in ["PRAGMA writable_schema = 1;",
    #              "DELETE FROM sqlite_master;",
    #              "PRAGMA writable_schema = 0;",
    #              "VACUUM;",
    #              "PRAGMA integrity_check;"]:
    #     db.execute(call)

    # db.isolation_level = ''
    # cursor = db.cursor()
    # cursor.execute("""
    # CREATE TABLE users (
    #     id integer PRIMARY KEY,
    #     login text NOT NULL UNIQUE,
    #     password text NOT NULL
    # )
    # """)
    #
    # cursor.execute('''
    #     CREATE TABLE rooms (
    #         id integer PRIMARY KEY,
    #         password text NOT NULL,
    #         owner_id integer NOT NULL,
    #         FOREIGN KEY (owner_id) REFERENCES users (id)
    #     )
    # ''')
    #
    # cursor.execute('''
    #     CREATE TABLE joined_rooms (
    #         id integer PRIMARY KEY,
    #         room_id integer NOT NULL,
    #         user_id integer NOT NULL,
    #         FOREIGN KEY (user_id) REFERENCES users (id) ,
    #         FOREIGN KEY (room_id) REFERENCES rooms (id) ,
    #         UNIQUE(room_id, user_id)
    #     )
    # ''')
    #
    # cursor.execute('''
    #     CREATE TABLE topics (
    #         id integer PRIMARY KEY,
    #         room_id integer NOT NULL UNIQUE,
    #         value text NOT NULL,
    #         FOREIGN KEY (room_id) REFERENCES rooms (id)
    #     )
    # ''')
    #
    # cursor.execute('''
    #     CREATE TABLE votes (
    #         id integer PRIMARY KEY,
    #         topic_id integer NOT NULL,
    #         user_id integer NOT NULL,
    #         value float NOT NULL,
    #         FOREIGN KEY (topic_id) REFERENCES topics (id),
    #         FOREIGN KEY (user_id) REFERENCES users (id),
    #         UNIQUE (user_id, topic_id)
    #     )
    # ''')
