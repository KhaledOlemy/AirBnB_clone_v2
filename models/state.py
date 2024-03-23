#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """
    State class -> table `states`
    cols;   name: string(128), not nullable

    cascade relation to citites.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            all_objects = models.storage.all()
            out_list = []
            for obj in all_objects:
                if obj.split('.')[0] == "City":
                    if all_objects[obj].state_id == self.id:
                        out_list.append(all_objects[obj])
            return out_list
