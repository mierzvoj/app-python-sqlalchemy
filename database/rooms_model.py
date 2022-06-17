from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from database.users_model import Base


class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    password = Column(String(12))
    users = relationship("User", back_populates="rooms")
    children = relationship("Topic", back_populates="rooms")
    def __repr__(self):
        return f"Room(id={self.id!r}, password={self.password!r})"


class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    rooms = relationship(
        "Room", back_populates="children"
    )
    value = Column(String(30))


def init_model(db):
    Base.metadata.create_all(db)
