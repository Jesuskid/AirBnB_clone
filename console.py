#/usr/bin/bash python3
"""Module defines the Console class"""
import  cmd

class  HBNBCommand(cmd.Cmd):
    """
      Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the Program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def emptyline(self) -> bool:
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
