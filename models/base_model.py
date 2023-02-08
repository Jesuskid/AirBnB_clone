#!/usr/bin/python3
"""
Creates a base Class called BaseModel
"""
import datetime
import uuid
import models


class BaseModel():
    """Base Model
    """
    def __init__(self):
        """Initialize a new BaseModel."""

        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """return the print str representation of th BaseModel
        """
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """Updates the update_at with current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance."""
        dict = self.__dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
