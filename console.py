#!/usr/bin/env python3
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the command interpreter for the HBNB project."""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """This command quits to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the Program with EOF (Ctrl+D)."""
        print()  # Ensure a new line before exiting.
        return True

    def emptyline(self):
        """Override the empty line behavior to do nothing."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
