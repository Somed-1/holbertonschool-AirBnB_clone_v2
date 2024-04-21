#!/usr/bin/pydoc3
"""db storage"""
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# Enviropment variables
USER = os.getenv('HBNB_MYSQL_USER')
PASSWORD = os.getenv('HBNB_MYSQL_PWD')
HOST = os.getenv('HBNB_MYSQL_HOST')
DB = os.getenv('HBNB_MYSQL_DB')


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Init method"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(USER, PASSWORD, HOST, DB),
            pool_pre_ping=True
        )
        if 'test' in sys.argv:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """All method"""
        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls)
        else:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())

        return {
            "{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs
        }

    def new(self, obj):
        """New method"""
        self.__session.add(obj)

    def save(self):
        """Save method"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete method"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """realod method"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close method"""
        self.__session.close()
        return self.__session
