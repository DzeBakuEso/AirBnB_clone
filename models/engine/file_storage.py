#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    """here we handles serialization and deserialization of BaseModel instances."""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}            # Dictionary to store objects

    def all(self):
        """Returns the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets a new object in __objects with key '<obj class name>.id'."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes JSON file to __objects, if the file exists."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value["__class__"]
                if cls_name == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
