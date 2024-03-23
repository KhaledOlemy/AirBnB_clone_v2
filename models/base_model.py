#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import mapped_column
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # id = Column(String(60), unique=True, nullable=False, primary_key=True)
    # created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    # updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    id = mapped_column(String(60), unique=True, nullable=False, primary_key=True, sort_order=-3)
    created_at = mapped_column(DateTime, nullable=False, default=(datetime.utcnow()), sort_order=-2)
    updated_at = mapped_column(DateTime, nullable=False, default=(datetime.utcnow()), sort_order=-1)
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs['updated_at'] = datetime.now()
            self.updated_at = kwargs['updated_at']
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs['created_at'] = datetime.now()
            self.created_at = kwargs['created_at']
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary['__class__'] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        models.storage.delete(self)
