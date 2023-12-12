#!/usr/bin/python3
"""importing from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User inheriting from BaseModel"""

    """public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
