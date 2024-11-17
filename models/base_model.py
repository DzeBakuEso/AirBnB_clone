from datetime import datetime
import uuid
from models import storage

class BaseModel:
    """Base class for all models in the application."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance or recreate from dictionary."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Update `updated_at` timestamp and save to storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """String representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
