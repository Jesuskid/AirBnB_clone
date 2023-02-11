#!/usr/bin/python3
"""
Creates an Amenity Class
"""
from models import base_model


class Amenity(base_model.BaseModel):
    """Represents an Amenity class that inherits form the BaseModel

    Attributes:
        name: name of the amenity
    """
    name = ""
