#!/usr/bin/python3
"""DBStorage Module"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """class DBStorage that
serializes instances to a JSON file and
deserializes JSON file to instances"""

    __engine = None
    __session = None

    def __init__(self):
        """__init__
        initializing DbStorage
        """

        self.__engine = create_engine(
            "mysql+mysqldb://{0}:{1}@{2}:3306/{3}".format(
                getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        self.reload()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name (argument cls)"""
        Base.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)

        if cls:
            cls = eval(cls.__name__)
            my_query = self.__session.query(cls).all()
        else:
            my_objs = [User, Place, Review, City, State, Amenity]
            my_query = []
            for elem in my_objs:
                my_query.extend(self.__session.query(elem)).all()

        object_dict = dict()
        for obj in my_query:
            object_dict["{}.{}".format(type(obj).__name__, obj.id)] = obj

        return object_dict

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database
        session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        create the current database session (self.__session)
         from the engine (self.__engine)"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine,
                            expire_on_commit=False)
        self.__session = scoped_session(sess)

    def close(self):
        """call close() method on the private session
        attribute (self.__session)"""
        self.__session.close()
