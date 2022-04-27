from sqlalchemy.orm import Session

class DAOBase:
    def __init__(self, engine):
        self._engine = engine
        self._session = None
    
    def open_session(self):
        """Create the session"""
        self._session = Session(self._engine)
        
    def rollback(self, message):
        """Roll back session"""
        self._session.rollback()
        print(message)
        
    def commit(self, message):
        """Commit session"""
        self._session.commit()
        print(message)
      