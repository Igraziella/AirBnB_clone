#!/usr/bin/python3
<<<<<<< HEAD
import uuid
from datetime import datetime

""" This module defines a class `BaseModel` """


class BaseModel():
    """ defines all common attributes/methods for other classes """

    def __init__(self):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Defines the string representation of the instance """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute `updated_at`
            with the current datetime
        """

        self.updated_at = datetime.now()


    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of `__dict__` of the instance
        """

        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
=======
""" base model module """

import uuid
import datetime from datetime


class BaseModel:
    """ defines a class BaseModel """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoforma()
>>>>>>> 1231c91d86ed7af969029b5d450adec54186f0bf
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
