#!/usr/bin/python3
"""
Creates a Review Class
"""
from models import base_model


class Review(base_model.BaseModel):
    """Represents a Review class that inherits form the BaseModel

    Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
