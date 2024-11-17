#!/usr/bin/python3
"""Defines the HBNBCommand class."""
import cmd
from models import storage
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def do_create(self, args):
        """Creates a new instance of a class."""
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[args]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Shows the string representation of an instance."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """Shows all string representations of instances."""
        if args and args not in self.classes:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in storage.all().values():
            if not args or obj.__class__.__name__ == args:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, args):
        """Updates an instance based on class name and id."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        obj.save()


if __name__ == "__main__":

    HBNBCommand().cmdloop()
