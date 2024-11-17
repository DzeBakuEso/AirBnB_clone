from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Base class for all models."""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Import `storage` here to avoid circular dependency
            from models import storage
            storage.new(self)

    def save(self):
        """Updates `updated_at` and saves to storage."""
        self.updated_at = datetime.now()
        # Import `storage` here to avoid circular dependency
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary of the instance."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """String representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
#!/usr/bin/python3 
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Base class for all models."""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Import `storage` here to avoid circular dependency
            from models import storage
            storage.new(self)

    def save(self):
        """Updates `updated_at` and saves to storage."""
        self.updated_at = datetime.now()
        # Import `storage` here to avoid circular dependency
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary of the instance."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """String representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
