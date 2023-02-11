#!/usr/bin/python3
"""
Creates a State Class
"""
from models import base_model


class State(base_model.BaseModel):
    """Represents a State class that inherits form the BaseModel

    Attributes:
        name: name of the state
    """
    name = ""
