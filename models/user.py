#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """ Represents a user.

    Attributes:
    first_name (str): first name of the user.
    last_name (str): last name of the user.
    email (str): email of the user.
    password (str): password of the user.
    """

    first_name = ""
    last_name = ""
    email = ""
    password = ""
