import sys
import json
import time
from random import random
from setup import *

command_list = {}

def command(function):
    command_list[function.__name__] = function.__doc__
    user["commands"].append(function.__name__)
    return function
    
def unlockable_command(function):
    if function.__name__ in user["commands"]:
        command_list[function.__name__] = function.__doc__
    def function_wrap(*args):
        if function.__name__ in user["commands"]:
            function(*args)
        else:
            print("Invalid command.")
    return function_wrap
    
@command
def help(command=None):
    """Prints this help message."""
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
            
@command            
def add():
    """Gives you points."""
    if user["total_version"] < 3:
        user["points"] += user["point_increment"]
        user["add_command_uses"] += 1
        if user["point_increment"] == 1:
            print("Added " + str(user["point_increment"]) + " point.")
        else:
            print("Added " + str(user["point_increment"]) + " points.")
        if user["add_command_uses"] == 20:
            user["commands"].append("update")
            command_list["update"] = "Updates the system, if there is a new update available."
            new_update("'buy' command to buy software to allow you to gain more points.", one_dot_one)
        if user["points"] >= 1500 and user["total_version"] < 3 and user["new_version"] is False:
            new_update("Minor bugfixes.")
    else:
        print("NameError: 'point' does not exist")
        print("An error occurred while executing the 'add' command.")
        
@command
def points():
    """Prints your points."""
    print("You have " + str(user["points"]) + " points.")
    
@command
def save():
    """Saves your variables to a save.json file."""
    with open('save.json', 'w+') as f:
        save = {
            "user": user,
            "software_prices": software_prices,
            "software_list": software_list
        }
        json.dump(save, f)
    print("Saved successfully! It is now safe to use the 'exit' command to exit the game.")

@command    
def exit():
    """Exits the game WITHOUT SAVING. Be careful with this command!"""
    sys.exit()
    
@unlockable_command
def update():
    """Updates the system, if there is an update available."""
    if user["new_version"]:
        print("Updating...")
        time.sleep(5)
        user["total_version"] += 1
        user["display_version"][1] += 1
        if user["display_version"][1] == 10:
            user["display_version"][0] += 1
            user["display_version"][1] = 0
        user["new_version"] = False
        print("IdlePY shell version a{}.{}".format(str(user["display_version"][0]), str(user["display_version"][1])))
        print("------------------------")
        print("What's new: " + user["update_message"])
        if user["update_function"] != False:
            function = user["update_function"]
            function()
            user["update_function"] = False
    else:
        print("There is no update available.")
        
@unlockable_command           
def buy(*item):
    """Buy software from the shop to get more points!"""
    item = " ".join(item)
    if not item:
        for entry in software_list:
            print(entry + ": " + software_list[entry] + " Costs " + str(software_prices[entry]) + " points.")
    else:
        valid_entry = False
        for entry in software_list:
            if item.lower() == entry.lower():
                valid_entry = True
                if user["points"] >= software_prices[entry]:
                    user["points"] -= software_prices[entry]
                    function = function_list[entry]
                    print("Successfully bought {} for {} points.".format(entry, software_prices[entry]))
                    software_prices[entry] = int(software_prices[entry] * 1.15)
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
            print("Software not found. Use 'buy' to see a list of available software.")
                
@unlockable_command
def ls():
    """Prints the folders and files in your current directory."""
    print("game shell home")
        
@unlockable_command
def badd(): 
    """An improved version of the add command!"""
    increment = user["point_increment"] * int((1 + random()))
    user["points"] += increment
    user["add_command_uses"] += 1
    if increment == 1:
        print("Added " + str(increment) + " point.")
    else:
        print("Added " + str(increment) + " points.")
            
# @command
# def runpy(*code):
    # """A command solely for developers. If you're seeing this message, you have a developer's copy of the game!"""
    # try:
        # exec(" ".join(code))
    # except Exception as error:
        # print("Failed to execute code.")
        # print(error)
        
def next_command():
    command = input('/shell>')
    command = command.split(" ")
    arguments = command[1:]
    command = command[0]
    if command in user["commands"]:
        try:
            globals()[command](*arguments)
        except TypeError as e:
            error = [int(s) for s in str(e).split() if s.isdigit()]
            print("Invalid usage. '{0}' takes {1} arguments but {2} were given. Use 'help {0}' for usage instructions.".format(function.__name__, error[0], error[1]))
    else:
        print("Invalid command.")