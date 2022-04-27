from .dao_base import DAOBase
from models.models import User
from sqlalchemy import select
class UsersDAO(DAOBase):
    table_name = "users"
    
    def __init__(self, engine):
        super().__init__(engine)
    
    def get_user_by_id(self, user_id):
        statement = select(User).filter_by(id=user_id)
        return self._session.execute(statement).all()
        
    