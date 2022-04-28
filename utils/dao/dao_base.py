from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
class DAOBase:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine
        self._session: Session = None
    
    def open_session(self):
        """Create the session"""
        self._session = Session(self._engine)
        
    def rollback(self, message: str):
        """Roll back session"""
        self._session.rollback()
        print(message)
        
    def commit(self, message: str):
        """Commit session"""
        self._session.commit()
        print(message)
        
    def close_session(self):
        """Give the connection back to the connection pool of Engine
        and doesn't close the connection"""
        self._session.close()
        
    def close_connection(self):
        """Close all connections of the connection pool"""
        self.close_session()
        self._engine.dispose()
      