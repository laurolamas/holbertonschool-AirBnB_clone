#!/usr/bin/python3
"""shebang"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """console por airbnb"""

    """task 6"""

    prompt = "(hbnb)"

    def do_quit(self, inp):
        """quit cmd function"""
        return True

    def do_EOF(self, inp):
        """EOF cmd function"""
        return True

    def help_EOF(self, inp):
        """documents EOF"""
        print("EOF")

    def help_quit(self, inp):
        """documents quit"""
        print("quit")

    def emptyline(self):
        pass

    """task 7"""

    def do_create(self, inp):
        """create instance, save json and print"""
        if inp == "":
            print("** class name missing **")
        else:
            try:
                object = eval(inp)()
                object.save()
                print(object.id)

            except Exception:
                print("** class doesn't exist **")

    def do_show(self, inp):
        """ Prints the string representation \
of an instance based on the class name and id"""

        string_split = inp.split()

        if len(string_split) == 0:
            print("** class name missing **")
        elif len(string_split) == 1:
            print("** instance id missing **")

        else:
            try:
                eval(string_split[0])
                try:
                    stored_d = storage.all()
                    print(stored_d[f'{string_split[0]}.{string_split[1]}'])

                except Exception:
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

    def do_destroy(self, inp):
        """Deletes an instance based on the class\
name and id (save the change into the JSON"""

        string_split = inp.split()

        if len(string_split) == 0:
            print("** class name missing **")
        elif len(string_split) == 1:
            print("** instance id missing **")

        else:

            try:
                eval(string_split[0])
                try:
                    del storage.all()[f'{string_split[0]}.{string_split[1]}']
                    storage.save()

                except Exception:
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

    def do_all(self, inp):
        """Prints all string representation of all\ 
instances based or not on the class name"""

        string_split = inp.split()

        if len(string_split) == 0:

            data_print = storage.all()
            size_getter = []

            for key in data_print:
                size_getter.append(key)

            print("[", end="")
            for cycle, key in enumerate(data_print):

                if cycle != len(size_getter) - 1:
                    print(f"\"{data_print[key]}\"", end=", ")
                else:
                    print(f"\"{data_print[key]}\"", end="")
            print("]")

        elif len(string_split) == 1:

            try:
                data_print = storage.all()
                for key in data_print:
                    if string_split[0] in key:
                        print(data_print[key])

            except Exception:
                print("** class doesn't exist **")

    def do_update(self, inp):
        """Updates an instance based on class name\
and id by adding or updating attribute"""

        string_split = inp.split()

        if len(string_split) == 0:
            print("** class name missing **")
        elif len(string_split) == 1:
            print("** instance id missing **")
        elif len(string_split) == 2:
            print("** attribute name missing **")
        elif len(string_split) == 3:
            print("** value missing **")

        else:

            try:
                eval(string_split[0])

                try:
                    for key, value in storage.all().items():
                        obj = value
                        if key == f"{string_split[0]}.{string_split[1]}":
                            setattr(obj, string_split[2], string_split[3])
                except Exception:
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
