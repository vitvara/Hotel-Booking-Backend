from utils.dao import DAO
from sqlalchemy import create_engine

engine = create_engine('sqlite:///hotel.db')
room = DAO(engine).table('room')
room.open_session()
room.book_room(1,1)
room.confirm_room(1,1)
# room.reset_room(1,1)

