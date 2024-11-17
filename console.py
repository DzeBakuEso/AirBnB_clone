#!/usr/bin/python3
"""Entry point for the HBNB command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)."""
        print()  # To ensure a new line before exiting.
        return True

    def emptyline(self):
        """Override empty line behavior to do nothing."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
