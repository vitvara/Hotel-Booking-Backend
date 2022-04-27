from cgitb import reset
from .dao_base import DAOBase
from sqlalchemy import select
from models.models import Room

class RoomDAO(DAOBase):
    
    def __init__(self, engine):
        super().__init__(engine)

    def book_room(self, room_id, user_id):
        self._session.query(Room).filter(Room.id==room_id).update({'status': 'pending', 'user_id':user_id})
        try:
            self.commit(f"Successfully Booking the room id={room_id}| user_id={user_id}")
        except:
            self.rollback(f"Failed booking the room id={room_id}| user_id={user_id}")
        finally:
            self._session.close()
            
    def confirm_room(self, room_id, user_id):
        self._session.query(Room).filter(Room.id==room_id).update({'status': 'reserved'})
        try:
            self.commit(f"Comfirmed Booking the room id={room_id}| user_id={user_id}")
        except:
            self.rollback(f"Failed to confirmed booking something \
                was wrong please try again the room id={room_id}| user_id={user_id}")
        finally:
            self._session.close()
            
    def reset_room(self, room_id, user_id):
        self._session.query(Room).filter(Room.id==room_id).update({'status': 'avaliable', 'user_id':None})
        try:
            self.commit(f"Successfully reset the room id={room_id}| user_id={user_id}")
        except:
            self.rollback(f"Failed to reset room, something \
                was wrong please try again the room id={room_id}| user_id={user_id}") 
        finally:
            self._session.close()
            
    def get_avaliable_room(self):
        statement = select(Room).filter_by(status="avaliable")
        return self._session.execute(statement).all()
    
    def get_all_room(self):
        statement = select(Room)
        return self._session.execute(statement).all()
    
    def get_room_by_user_id(self, user_id):
        statement = select(Room).filter_by(user_id=user_id)
        return self._session.execute(statement).all()
    
    def __repr__(self) -> str:
        return f"RoomDAO(engine={self._engine}, session={self._session})"