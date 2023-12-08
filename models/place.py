#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Represents a place.

    Attributes:
    name (str): name of the place.
    user_id (str): id of the user.
    city_id (str): id of the city
    description (str): description of the place.
    number_of_rooms (int): number of rooms in the place
    number_of_bathrooms (int)
    max_guest(int): maximum guests the place can accomodate.
    latitude (float)
    longitude (float)
    amenity_id (list): a list of amenity ids
    """
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_of_rooms = 0
    number_of_bathrooms = 0
    max_guest = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []
