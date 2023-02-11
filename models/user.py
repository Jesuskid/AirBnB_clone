#!/usr/bin/python3
"""
Creates a User Class
"""
from models import base_model


class User(base_model.BaseModel):
    """Represents a User class that inherits form the BaseClass

    Attributes:
        email: user email
        password: user password
        first_name: user first_name
        last_name: user last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
