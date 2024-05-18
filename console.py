#!/usr/bin/python3
""" console """

import cmd
from ModelFunctions import ModelFucntions 
from models import storage
from sqlalchemy.exc import SQLAlchemyError

class SentinelCommand(cmd.Cmd):
    """ Sentinel console """
    prompt = '(Sentinel|Dev) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class"""
        ModelFucntions.create_instance(arg)
        

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        ModelFucntions.show_instance(arg)
        

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        ModelFucntions.destroy_instance(arg)
    
    def do_changedbg(self, arg):
        """
        Switches Databases
        """

        try:
            storage.switch_database(arg)
        except SQLAlchemyError as e:
            print(f"Error switching database: {e}")

    def do_all(self, arg):
        """Prints string representations of instances"""
        ModelFucntions.show_all_instances(arg)
        
    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        ModelFucntions.update_instance(arg)
        
if __name__ == '__main__':
    SentinelCommand().cmdloop()
