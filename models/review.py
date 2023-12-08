#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Represents user review.

    Attributes:
    user_id (str): id of the user.
    text (str): review text
    place_id (str): place id (duh).
    """

    user_id = ""
    text = ""
    place_id = ""
