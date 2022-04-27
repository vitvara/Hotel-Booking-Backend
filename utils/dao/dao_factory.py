from enum import Enum
from sqlalchemy import table
from sqlalchemy.orm import Session

from utils.dao.dao_base import DAOBase
from .dao_room import RoomDAO
from .dao_users import UsersDAO



class DAOClasses(Enum):
    room = RoomDAO
    users = UsersDAO



class DAO:
    def __init__(self, engine):
        self.__engine = engine

    def table(self, table_name: str) -> DAOBase:
        """Get dao by table name

        Args:
            table_name (str): name of table in database

        Returns:
            DAOBase: DAO that selected from table name
        """
        dao = DAOClasses[table_name].value
        return dao(self.__engine)