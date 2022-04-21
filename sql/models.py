from sqlalchemy.orm import registry
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

mapper_registry = registry()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, name={self.username})"


class Hotel(Base):
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
