#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting from BaseModel class"""

    """
    public class attributes
    state_id = empty string: it will be the State.id
    name = empty string
    """

    state_id = ""
    name = ""
