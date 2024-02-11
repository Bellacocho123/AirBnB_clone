#!/usr/bin/python3
""" Module that defines all common attributes/methods for other classes """


import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Constructor method """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """ String representation of the BaseModel class """

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """ Updates the attribute updated_at with the current datetime """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ """

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
