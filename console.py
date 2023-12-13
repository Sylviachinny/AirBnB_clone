#!/usr/bin/python3


"""The AirBnB clone command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The class (hbnbcommand) using the cmd module """

    prompt = "(hbnb) "
    __classes = ["BaseModel",
                 "User",
                 "Place",
                 "State",
                 "City",
                 "Amenity",
                 "Review"
                 ]

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

    def do_create(self, arg):
        """creates a new instance.
        args = arg.split() is using whitespace to
        split the input string into list of arguments
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            theNew_object = eval(f"{args[0]}")()
            print(theNew_object.id)
            storage.save()

    def do_show(self, arg):
        """prints the string representation of an instance
        base on the class name and id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """deletes an instance based on class name and id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
        storage.save()

    def do_all(self, arg):
        """all instances are printed"""
        args = arg.split()

        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if
                   k.startswith(args[0])])

    def do_update(self, arg):
        """updates an instance"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_class = args[0]
            obj_id = args[1]
            obj_key = obj_class + "." + obj_id
            obj = storage.all()[obj_key]

            attr_name = args[2]
            attr_value = args[3]

            if attr_value[0] == '"':
                attr_value = attr_value[1:-1]

            if hasattr(obj, attr_name):
                type_attr = type(getattr(obj, attr_name))
                if type_attr in [str, float, int]:
                    attr_value = type_attr(attr_value)
                    setattr(obj, attr_name, attr_value)
            else:
                setattr(obj, attr_name, attr_value)
            storage.save()

    def default(self, arg):
        """to retrieve all instances of a class"""
        args = arg.split('.')
        if args[0] in self.__classes:
            if args[1] == "all()":
                """
                using the instance all() to retrieve a class
                """
                self.do_all(args[0])
            elif args[1] == "count()":
                """
                using the attributes count() to list
                the number of class
                """
                count_args = [v for k, v in storage.all()
                              .items() if k.startswith(args[0])]
                print(len(count_args))
            elif args[1].startswith("show"):
                """print(args[0])"""
                """print(args[1])"""
                id_show = args[1].split('"')[1]
                print(id_show)
                self.do_show(f"{args[0]} {id_show}")
            elif args[1].startswith("destroy"):
                id_destroy = args[1].split('"')[1]
                print(id_destroy)
                self.do_destroy(f"{args[0]} {id_destroy}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
