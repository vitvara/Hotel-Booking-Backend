from .dao_base import DAOBase

class UsersDAO(DAOBase):
    table_name = "users"
    
    def __init__(self, engine):
        super().__init__(engine)
        
    