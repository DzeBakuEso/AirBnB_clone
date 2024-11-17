#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, & prints the id."""
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        instance = self.classes[args]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Prints string represention of insnce based on class name & id."""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        key = f"{tokens[0]}.{tokens[1]}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, args):
        """Deletes an instance based on class name and id."""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        key = f"{tokens[0]}.{tokens[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """Prints all string representations of instances."""
        if args and args not in self.classes:
            print("** class doesn't exist **")
            return
        instances = storage.all()
        results = []
        for key, obj in instances.items():
            if not args or key.startswith(args):
                results.append(str(obj))
        print(results)

    def do_update(self, args):
        """Updates an innce bsed on clas nam & id by adng/updtng attribute."""
        tokens = args.split()
        if len(tokens) < 1:
            print("** class name missing **")
            return
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = f"{tokens[0]}.{tokens[1]}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return
        if len(tokens) < 3:
            print("** attribute name missing **")
            return
        if len(tokens) < 4:
            print("** value missing **")
            return
        attr_name = tokens[2]
        attr_value = tokens[3].strip('"')

        # Cast attribute value to the correct type
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                print("** invalid value type **")
                return
        setattr(instance, attr_name, attr_value)
        instance.save()

    def emptyline(self):
        """Override the empty line behavior to do nothing."""
        pass

    def do_quit(self, args):
        """Exits the program."""
        return True

    def do_EOF(self, args):
        """Exits the program with EOF (Ctrl+D)."""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
