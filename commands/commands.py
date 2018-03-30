import time
from random import random
from setup import *
import commands_decorator as commands
    
@commands.command(True)
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
        if user["update_function"] is not False:
            function = user["update_function"]
            function()
            user["update_function"] = False
    else:
        print("There is no update available.")
        
@commands.command(True)           
def buy(*item):
    """Buy software from the shop to get more points!"""
    item = " ".join(item)
    if not item:
        for entry in software_list:
            print(entry + ": " + software_list[entry] + " Costs " + str(software_prices[entry]) + " points.")
    else:
        if user["total_version"] == 3 and item.lower() != "python" and item.lower() != "betteradd":
            print("aogaogjpaotjpatj")
            return
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
            if repeatable[bought_entry] is False:
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
                
@commands.command(True)
def ls():
    """Prints the folders and files in your current directory."""
    print("game shell home")
        
@commands.command(True)
def badd(): 
    """An improved version of the add command!"""
    increment = int(user["point_increment"] * (1 + (random() / 2)))
    user["points"] += increment
    user["add_command_uses"] += 1
    if increment == 1:
        print("Added " + str(increment) + " point.")
    else:
        print("Added " + str(increment) + " points.")
            
# @commands.command(False)
# def runpy(*code):
    # """A command solely for developers. If you're seeing this message, you have a developer's copy of the game!"""
    # try:
        # exec(" ".join(code))
    # except Exception as error:
        # print("Failed to execute code.")
        # print(type(error).__name__ + ": " + str(error))