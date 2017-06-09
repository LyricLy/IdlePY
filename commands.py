import sys
import json
import time
from random import random
from variable_setup import *
 
def command(unlockable):
    def command_decorator(function):
        function_list[function.__name__] = function
        def wrapped(*args):
            if unlockable == True:
                if function.__name__ in user["commands"]:
                    function(*args)
                else:
                    print("Invalid command.")
            else:
                function(*args)
        return wrapped
    return command_decorator
    
def next_command():
    command = input('/shell>')
    command = command.split(" ")
    arguments = command[1:]
    command = command[0]
    try:
        function = function_list[command]
        function(*arguments)
    except KeyError:
        print("Invalid command.")
    except TypeError as e:
        error = [int(s) for s in str(e).split() if s.isdigit()]
        print("Invalid usage. '{0}' takes {1} arguments but {2} we{3} given. Use 'help {0}' for usage instructions.".format(function.__name__, error[0], error[1]))
        
@command(False)
def help(command=None):
    if command != None:
        subcommand = False
        for entry in command_list:
            if command == entry:
                print(str(entry) + ": " + command_list[entry])
                subcommand = True
        if subcommand == False: print("That is not a valid command.")
    else:
        for entry in command_list:
            print(str(entry) + ": " + command_list[entry])
            
@command(False)
def add():
    if user["version"] < 1.2:
        user["points"] += user["point_increment"]
        user["add_command_uses"] += 1
        if user["point_increment"] == 1:
            print("Added " + str(user["point_increment"]) + " point.")
        else:
            print("Added " + str(user["point_increment"]) + " points.")
        if user["add_command_uses"] == 20:
            user["commands"].append("update")
            command_list["update"] = "Updates the system, if there is a new update available."
            new_update("'buy' command to buy software to allow you to gain more points. Subcommands: view", one_dot_one)
        if user["points"] >= 1500 and user["version"] < 1.2 and user["new_version"] is False:
            new_update("Minor bugfixes.")
    else:
        print("NameError: 'point' does not exist")
        print("An error occurred while executing the 'add' command.")
        
@command(False)
def points():
    print("You have " + str(user["points"]) + " points.")
    
@command(False)
def save():
    with open('save.json', 'w+') as f:
        save = {
            "user": user,
            "software_prices": software_prices
        }
        json.dump(save, f)
    print("Saved successfully! It is now safe to use the 'exit' command to exit the game.")
        
@command(False)        
def exit():
    sys.exit()
    
@command(True)    
def update():
    if user["new_version"]:
        print("Updating...")
        time.sleep(5)
        user["version"] += 0.1
        user["new_version"] = False
        print("IdlePY shell version a" + str(user["version"]))
        print("------------------------")
        print("What's new: " + user["update_message"])
        if user["update_function"] != False:
            function = user["update_function"]
            function()
            user["update_function"] = False
        else:
            print("There is no update available.")
            
@command(True)            
def buy(*item):
    item = " ".join(*item)
    if item == "view":
        for entry in software_list:
            print(entry + ": " + software_list[entry] + " Costs " + str(software_prices[entry]) + " points.")
    else:
        valid_entry = False
        for entry in software_list:
            if item == entry:
                valid_entry = True
                if user["points"] >= software_prices[entry]:
                    user["points"] -= software_prices[entry]
                    function = function_list[entry]
                    print("Successfully bought {} for {} points.".format(entry, entry_split[1]))
                    software_prices[entry] *= 1.15
                    bought_entry = entry
                    function()
                else:
                    print("Insufficient funds.")
        try:
            if repeatable[bought_entry] == False:
                software_list.pop(bought_entry)
        except NameError:
            pass
        try: 
            software_list.update(software_list_temp)
            sofware_list_temp.clear()
        except NameError:
            pass 
        if not valid_entry:
            print("Software not found. Use 'buy view' to see a list of available software.")
                
@command(True)
def ls():
    print("game shell home")
        
@command(True)
def badd():       
    user["points"] += user["point_increment"] * int((1 + random()))
    user["add_command_uses"] += 1
    if user["point_increment"] == 1:
        print("Added " + str(user["point_increment"]) + " point.")
    else:
        print("Added " + str(user["point_increment"]) + " points.")
            
@command(False)
def runpy(*code):
    try:
        exec(" ".join(*code))
    except Exception as error:
        print("Failed to execute code.")
        print(error)