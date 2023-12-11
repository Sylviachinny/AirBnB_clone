#!/usr/bin/python3

"""The import modules"""
import uuid
from datetime import datetime


class BaseModel():
    """The class Basemodel"""

    def __init__(self):
        """ The public instance attributes"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """using __str__ representation to print
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """The public instance method
        that saves the updated datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """using dict_copying to contain
        all keys/values
        """
        dict_copying = self.__dict__.copy()
        dict_copying["__class__"] = self.__class__.__name__
        dict_copying["created_at"] = self.created_at.isoformat()
        dict_copying["updated_at"] = self.updated_at.isoformat()
        return dict_copying
