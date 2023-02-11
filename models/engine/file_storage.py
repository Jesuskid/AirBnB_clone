#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Represents the Storage engine
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dict __objects"""
        return FileStorage.__objects

    def new(self, obj):
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """Serialize __objects to JSON file path"""
        object_dict = FileStorage.__objects
        new_object_dict = {obj: object_dict[obj].to_dict() for obj in object_dict.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_object_dict, file)

    def reload(self):
        """Deserializes the __objects from JSON file"""
        try:
            with open('file.json', 'r') as file:
                object_dict = json.load(file)
                for val in object_dict.values():
                    cls_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(cls_name)(**val))
        except FileNotFoundError:
            return

