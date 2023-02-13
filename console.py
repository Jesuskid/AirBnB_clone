#/usr/bin/bash python3
"""Module defines the Console class"""
import  cmd
from models.base_model import BaseModel
from models import storage
import re
from shlex import  split

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class  HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command(hbnb) prompt.
    """

    prompt = "(hbnb) "

    __classes =  {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the Program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def emptyline(self) -> bool:
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        arg_val = arg.split(" ")
        if len(arg_val[0]) == 0:
            print("** class name missing **")
        elif arg_val[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_val[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id>
        Displays the string representation of a class instance of a given id.
        """
        arg_val = arg.split(" ")
        object_dict = storage.all()
        if len(arg_val[0]) == 0:
            print("** class name missing **")
        elif arg_val[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_val) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_val[0], arg_val[1]) not in object_dict:
            print("** no instance found **")
        else:
            print(object_dict["{}.{}".format(arg_val[0], arg_val[1])])

    def do_destroy(self, arg):
        """Usage: destroys <class> <id>
        Delete a class instance of a given id."""
        arg_val = arg.split(" ")
        object_dict = storage.all()
        if len(arg_val[0]) == 0:
            print("** class name missing **")
        elif arg_val[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_val) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_val[0], arg_val[1]) not in object_dict:
            print("** no instance found **")
        else:
            del object_dict["{}.{}".format(arg_val[0], arg_val[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arg_val = arg.split(" ")
        if len(arg_val) > 0 and arg_val[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(arg_val) > 0 and arg_val[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(arg_val) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name> "<attribute value>
        Only one attribute can be updated at the time
        You can assume the attribute name is valid (exists for this model)
        The attribute value must be casted to the attribute type
        """
        arg_val = parse(arg)
        objdict = storage.all()

        #checks
        print(arg_val[2])
        if len(arg_val) == 0:
            print("** class name missing **")
            return False
        if arg_val[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_val) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_val[0], arg_val[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arg_val) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_val) == 3:
            try:
                type(eval(arg_val[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_val) == 4:
            obj = objdict["{}.{}".format(arg_val[0], arg_val[1])]
            if arg_val[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_val[2]])
                obj.__dict__[arg_val[2]] = valtype(arg_val[3])
            else:
                obj.__dict__[arg_val[2]] = arg_val[3]
        elif type(eval(arg_val[2])) == dict:
            obj = objdict["{}.{}".format(arg_val[0], arg_val[1])]
            for k, v in eval(arg_val[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
