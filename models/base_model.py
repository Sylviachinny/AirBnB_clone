#!/usr/bin/python3

"""The import modules"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """The class Basemodel"""

    def __init__(self, *args, **kwargs):
        """ The public instance attributes
            *args: arguments
            **kwargs: key-word arguments
        """

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """using __str__ representation to print
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """The public instance method
        that saves the updated datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """using dict_copying to contain
        all keys/values
        """
        dict_copying = self.__dict__.copy()
        dict_copying["__class__"] = self.__class__.__name__
        dict_copying["created_at"] = self.created_at.isoformat()
        dict_copying["updated_at"] = self.updated_at.isoformat()
        return dict_copying
