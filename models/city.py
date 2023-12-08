#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents a city.

    Attributes:
    name (str): name of the city.
    state_id (str): id of the state.
    """

    name = ""
    state_id = ""
