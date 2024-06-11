from setup import *

command_list = {}

def command(unlockable):
    def command_wrapper(function):
        command_list[function.__name__] = function.__doc__
        if not unlockable:
            user["commands"].append(function.__name__)
        return function
    return command_wrapper
