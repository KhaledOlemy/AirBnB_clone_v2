#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    City class -> table `cities`
    cols;   name: string(100), not nullable
            state_id: string(60), not nullable, FK-> states.id
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")