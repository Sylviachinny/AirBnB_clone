#!/usr/bin/python3

"""importing class BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """the class Review inherits from BaseModel class

    public class attributes
    place_id = empty string: it will be the place.id
    user_id = empty string: it will be the user.id
    text = empty string

    """

    place_id = ""
    user_id = ""
    text = ""
