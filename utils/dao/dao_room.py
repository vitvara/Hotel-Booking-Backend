from cgitb import reset
from typing import List
from .dao_base import DAOBase
from sqlalchemy import select, Engine
from models.models import Room

class RoomDAO(DAOBase):
    
    def __init__(self, engine: Engine):
        super().__init__(engine)
        
    def book_room(self, room_id: int, user_id: int) -> None:
        """Update room status to `pending`

        Args:
            room_id (int)
            user_id (int)
        """
        self._session.query(Room).filter(Room.id==room_id).update({'status': 'pending', 'user_id':user_id})
        try:
            self.commit(f"Successfully Booking the room id={room_id}| user_id={user_id}")
        except:
            self.rollback(f"Failed booking the room id={room_id}| user_id={user_id}")
        finally:
            self._session.close()
            
    def confirm_room(self, room_id: int, user_id: int) -> None:
        """Update room status to `reserved`

        Args:
            room_id (int)
            user_id (int)
        """
        self._session.query(Room).filter(Room.id==room_id).update({'status': 'reserved'})
        try:
            self.commit(f"Comfirmed Booking the room id={room_id}| user_id={user_id}")
        except:
            self.rollback(f"Failed to confirmed booking something \
                was wrong please try again the room id={room_id}| user_id={user_id}")
        finally:
            self._session.close()
            
    def reset_room(self, room_id: int, user_id: int) -> None:
        """Reset room to default

        Args:
            room_id (int)
            user_id (int)
        """
        self._session.query(Room).filter(Room.id==room_id).update({'status': 'avaliable', 'user_id':None})
        try:
            self.commit(f"Successfully reset the room id={room_id}| user_id={user_id}")
        except:
            self.rollback(f"Failed to reset room, something \
                was wrong please try again the room id={room_id}| user_id={user_id}") 
        finally:
            self._session.close()
            
    def get_avaliable_room(self) -> List[Room]:
        """Query all room that avaliable
        Returns:
            List[Room]: List of room from querying all room that avaliable
        """
        statement = select(Room).filter_by(status="avaliable")
        return self._session.execute(statement).all()
    
    def get_all_room(self) -> List[Room]:
        """Query all room

        Returns:
            List[Room]: List of all room in database
        """
        statement = select(Room)
        return self._session.execute(statement).all()
    
    def get_room_by_user_id(self, user_id: int) -> List[Room]:
        """Query room filter by user id

        Args:
            user_id (int)

        Returns:
            List[Room]: List of room from querying by user id
        """
        statement = select(Room).filter_by(user_id=user_id)
        return self._session.execute(statement).all()
    
    def __repr__(self) -> str:
        return f"RoomDAO(engine={self._engine}, session={self._session})"