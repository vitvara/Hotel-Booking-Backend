from .dao_base import DAOBase
from models.models import User
from sqlalchemy import select
from sqlalchemy.engine import Engine
from typing import List
class UsersDAO(DAOBase):
    table_name = "users"
    
    def __init__(self, engine: Engine):
        super().__init__(engine)
    
    def get_user_by_id(self, user_id: int) -> List[User] :
        """Query user filter by id

        Args:
            user_id (int)

        Returns:
            List[User]: List of user from querying by user id
        """
        statement = select(User).filter_by(id=user_id)
        return self._session.execute(statement).all()
        
    def get_user_by_name(self, username: str) -> List[User]:
        """Query user filter by username

        Args:
            username (str)

        Returns:
            List[User]: List of user from querying by username
        """
        statement = select(User).filter_by(username=username)
        return self._session.execute(statement).all()