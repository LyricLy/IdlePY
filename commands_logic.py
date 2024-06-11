import commands
from setup import *
    
easter_eggs = {
    "xyzzy": "Nothing happens.",
    "spawn anime tiddy monster": "...what?"
} 
    
def next_command():
    query = input('/shell>')
    command = query.split(" ")
    arguments = command[1:]
    command = command[0]
    
    if query in easter_eggs:
        print(easter_eggs[query])
    elif command in user["commands"]:
        function = getattr(commands, command)
        try:
            function(*arguments)
        except TypeError as e:
            error = [int(s) for s in str(e).split() if s.isdigit()]
            print("Invalid usage. '{0}' takes {1} arguments but {2} were given. Use 'help {0}' for usage instructions.".format(function.__name__, error[0], error[1]))
    elif command:
        print("Invalid command.")
