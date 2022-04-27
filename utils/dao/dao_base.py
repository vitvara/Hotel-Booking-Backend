from sqlalchemy.orm import Session

class DAOBase:
    def __init__(self, engine):
        self._engine = engine
        self._session = None
    
    def open_session(self):
        self._session = Session(self._engine)
        
    def rollback(self, message):
        self._session.rollback()
        print(message)
        
    def commit(self, message):
        self._session.commit()
        print(message)
      