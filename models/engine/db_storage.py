#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in db storage format"""
    __engine = None
    __session = None

    def __init__(self):
        """
        init db storage
        """
        user = os.getenv('HBNB_MYSQL_USER')
        pswd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(user, pswd, host, db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        return all instances /or/ cls instances
        """
        out_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            classes = [cls]
        else:
            classes = [State, City, Amenity, Place, User, Review]
        for class_name in classes:
            class_instances = self.__session.query(class_name)
            for ins in class_instances:
                out_dict["{}.{}".format(type(ins).__name__, ins.id)] = ins
        return out_dict

    def new(self, obj):
        """
        create new obj
        """
        self.__session.add(obj)

    def save(self):
        """
        save and commit to db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete obj of db
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        reload objs from db
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """calls remove func"""
        self.__session.close()
