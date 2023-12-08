#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class State(BaseModel):
    """ Represents the state of the user.
    Attributes

    name (str) : name of the state.
    """

    name = ""
