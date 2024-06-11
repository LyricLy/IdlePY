import sys
import json
import base64
from setup import *
import commands_decorator as commands

@commands.command(False)
def help(command=None):
    """Prints this help message."""
    if command is not None:
        subcommand = False
        for entry in commands.command_list:
            if command == entry and entry in user["commands"]:
                print(str(entry) + ": " + commands.command_list[entry])
                subcommand = True
        if subcommand is False: 
            print("That is not a valid command.")
    else:
        for entry in commands.command_list:
            if entry in user["commands"]:
                print(str(entry) + ": " + commands.command_list[entry])
            
@commands.command(False)        
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
            new_update("'buy' command to buy software to allow you to gain more points.", "one_dot_one")
        if user["points"] >= 1500 and user["total_version"] < 3 and user["new_version"] is False:
            new_update("Minor bugfixes.")
    else:
        print("NameError: 'point' does not exist")
        print("An error occurred while executing the 'add' command.")
        
@commands.command(False)
def points():
    """Prints your points."""
    print("You have " + str(user["points"]) + " points.")
    
@commands.command(False)
def save():
    """Saves your variables to a save.json file."""
    with open('save.json', 'w+') as f:
        save = {
            "user": user,
            "software_prices": software_prices,
            "software_list": software_list
        }
        f.write(base64.b64encode(json.dumps(save).encode('utf-8')).decode('utf-8'))
    print("Saved successfully! It is now safe to use the 'exit' command to exit the game.")

@commands.command(False)  
def exit():
    """Exits the game WITHOUT SAVING. Be careful with this command!"""
    sys.exit()
    
# @commands.command(False)
# def runpy(*code):
    # """A command solely for developers. If you're seeing this message, you have a developer's copy of the game!"""
    # try:
        # exec(" ".join(code))
    # except Exception as error:
        # print("Failed to execute code.")
        # print(type(error).__name__ + ": " + str(error))
