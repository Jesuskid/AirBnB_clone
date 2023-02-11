#!/usr/bin/python3
"""
Creates a State Class
"""
from models import base_model


class City(base_model.BaseModel):
    """Represents a City class that inherits form the BaseModel

    Attributes:
        name: name of the city
        state_id: State Id
    """
    name = ""
    state_id = ""
