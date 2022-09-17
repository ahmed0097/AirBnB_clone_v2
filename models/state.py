#!/usr/bin/python3
"""State Module"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City
import models


class State(BaseModel, Base):
    """Class for State Objects
    Attributes:
    name: string - empty string
    """
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete')
    else:
        name = str()

        @property
        def cities(self):
            """Returns all cities that have the same id as
            self.id (State id)"""
            my_cities = list()
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    my_cities.append(city)
            return my_cities
