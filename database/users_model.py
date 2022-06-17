from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    # def __init__(self, id, login):
    #     self.id = id
    #     self.login = login
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(Text, nullable=False)
    password = Column(Text, nullable=False)

    rooms = relationship(
        "Room", back_populates="users", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id!r}, login={self.login!r}, password={self.password!r}"


def init_model(db):
    Base.metadata.create_all(db)
