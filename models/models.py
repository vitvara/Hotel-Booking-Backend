from sqlalchemy.orm import registry
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

mapper_registry = registry()
Base = declarative_base()


class User(Base):
    """user account"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)

    def __repr__(self):
        return f"User(id={self.id}, name={self.username})"


class Room(Base):
    """Room infomation

    room_number: room number in the building
    bed: number of bed
    status: Default=avaliable=> can be reserved 
                    pending=> working on payment of customer (customer hasn't pay yet)
                    full=> room already booked
    type: room type
    user_id: id of ther user that book the room; None if no one has reserved yet.
    """
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=False, nullable=False)
    room_number = Column(Integer, nullable=False)
    building = Column(String, nullable=False)
    floor = Column(Integer, nullable=False)
    bed = Column(Integer)
    max_guest = Column(Integer)
    status = Column(String, default="avaliable")
    user_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String)
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Hotel(id={self.id}, \
    room_number={self.room_number}, building={self.building}, \
    floor={self.floor}, bed={self.bed}, max_guest={self.max_guest},\
        status={self.status}, type={self.type}, price={self.price})"
