#!/usr/bin/python3

""" Module to handle console input/output"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class to handle console input/output """
    prompt = '(hbnb) '
    model_names = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
        ]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file"""
        if arg == "":
            print("** class name missing **")
            return
        if arg not in self.model_names:
            print("** class doesn't exist **")
            return
        obj = eval(arg)()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class"""
        if self.check_error(arg):
            return
        id = arg.split()[1]
        for _, value in storage.all().items():
            if value.id == id:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        if self.check_error(arg):
            return
        id = arg.split()[1]
        for key, value in storage.all().items():
            if value.id == id:
                del storage.all()[key]
                storage.save()
                return
        print("** no instance found **")

    def check_error(self, arg):
        """Helper function to check for class and id"""
        model, id = arg.split() + [""] * (2 - len(arg.split()))
        if model == "":
            print("** class name missing **")
            return True
        if model not in self.model_names:
            print("** class doesn't exist **")
            return True
        if id == "":
            print("** instance id missing **")
            return True
        return False

    def do_all(self, arg):
        """ Prints all string representation of all instances"""
        value_list = []
        if arg == "":
            for value in storage.all().values():
                value_list.append(str(value))
            print(value_list)
            return
        if arg not in self.model_names:
            print("** class doesn't exist **")
            return
        for value in storage.all().values():
            if value.__class__.__name__ == arg:
                value_list.append(str(value))
        print(value_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id"""
        items = []
        for i in arg.split():
            items.append(i)
        model = items[0] if len(items) > 0 else ""
        id = items[1] if len(items) > 1 else ""
        attr = items[2] if len(items) > 2 else ""
        value = items[3] if len(items) > 3 else ""

        if model == "":
            print("** class name missing **")
            return
        if model not in self.model_names:
            print("** class doesn't exist **")
            return
        if id == "":
            print("** instance id missing **")
            return
        if attr == "":
            print("** attribute name missing **")
            return
        if value == "":
            print("** value missing **")
            return

        for _, obj in storage.all().items():
            if obj.id == id:
                if hasattr(obj, attr):
                    value = type(getattr(obj, attr))(value)
                setattr(obj, attr, value)
                storage.save()
                return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
