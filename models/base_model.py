#!/usr/bin/env python3

import uuid
from datetime import datetime


class BaseModel:
    """

    This is Base class for all models

    """

    def __init__(self):

        """
        we initializes a new instance of BaseModel with its attributes

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at


    def save(self):
        """
        we updates the updated_at attribute to the current datetime.    

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Here we returns a dictionary representation of the instance.

        """
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name
        dict_repr["created_at"] = self.created.at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr

    def __str__(self):
        """
        Here we return a string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
