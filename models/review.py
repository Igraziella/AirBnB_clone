#!/usr/bin/python3
""" Creates a review module """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines a class - Review """
    place_id = ""
    user_id = ""
    text = ""
