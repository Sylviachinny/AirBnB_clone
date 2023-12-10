#!/usr/bin/python3


import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """This is an EOF to exit the program
        """
        return True

    def emptyline(self):
        """Method called when an empty line
        is entered in response to the prompt
        """
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
