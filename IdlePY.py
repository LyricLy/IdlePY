import sys
import json
import time
from random import random

user = {
    "points": 0,
    "point_increment": 1,
    "add_command_uses": 0,
    "commands": [],
    "software": [],
    "new_version": False,
    "update_message": "",
    "update_function": "",
    "version": 1.0,
    "for_testing": ""
}
command_list = {
    "help": "Prints this help message.",
    "add": "Gives you points.",
    "points": "Lists your points.",
    "save": "Saves all of your variables to a save.json file.",
    "exit": "Exits the game WITHOUT SAVING. Be careful with this command!"
}
software_list = {
    "Python": "A useful programming language that can allow you to program other software.$%1000$%python$%one_time",
    "ls": "Discover what files are on your system so that you can poke around with other software.$%800$%ls$%one_time",
    "PointHack": "Get more points with the 'add' command!$%50$%point_hack$%repeatable"
}
software_list_temp = {}
#functions for software from the shop that will trigger when software is bought
def python():
    user["software"].append("python")
    software_list_temp["Basic Bot"] = "Runs the add command once every five seconds.$%700$%basic_bot$%repeatable"
    software_list_temp["BetterAdd"] = "Adds an improved version of the add command, 'badd' with greater stability and point gaining.$%500$%better_add$%one_time"

def ls():
    user["software"].append("ls")
    user["commands"].append("ls")
    software_list_temp["vim"] = "A text editor that can be used to edit files. Could you possibly spoof some numbers?$%500$%vim$%one_time"
    software_list_temp["cd"] = "A useful tool to move around your system.$%300$%cd$%one_time"
    
def point_hack():
    software_list_temp["PointHack Pro"] = "The professional version of PointHack to increase your point multiplier even more.$%300$%point_hack$%repeatable"
    user["point_increment"] += 2
    
def better_add():
    user["software"].append("better_add")
    user["commands"].append("badd")
#functions for updates that trigger when an update completes
def one_dot_one():
    user["commands"].append("buy")
    command_list["buy"] = "Allows you to buy software to help you get more points. Subcommands: view"

    
#if a function needs to be called when only the name of the function as a string is available, this can be used to point to the function
function_list = {
    "python": python,
    "ls": ls,
    "point_hack": point_hack,
    "better_add": better_add
}
  
def new_update(update_message, function=False):
    print("You have a new update available to the operating system!")
    print("Use the 'update' command to update your system.")
    user["new_version"] = True
    user["update_message"] = update_message
    if function != False:
        user["update_function"] = function

def next_command():
    command = input('/shell>')
    
    if command.startswith("help ") or command == "help":
        commands = command.split(" ")
        commands.append("end")
        subcommand = False
        for entry in command_list:
            if commands[1] == entry:
                print(str(entry) + ": " + command_list[entry])
                subcommand = True
        if subcommand == False:
            for entry in command_list:
                print(str(entry) + ": " + command_list[entry])
                
    elif command.startswith("add ") or command == "add":
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
    elif command.startswith("points ") or command == "points":
        print("You have " + str(user["points"]) + " points.")
    elif command.startswith("save ") or command == "save":
        with open('save.json', 'w+') as f:
            json.dump(user, f)
        print("Saved successfully! It is now safe to use the 'exit' command to exit the game.")
            
    elif command.startswith("exit ") or command == "exit":
        sys.exit()
        
    elif command.startswith("update ") or command == "update":
        if not "update" in user["commands"]:
            print("Invalid command.")
        else:
            if user["new_version"]:
                print("Updating...")
                time.sleep(5)
                user["version"] += 0.1
                user["new_version"] == False
                print("IdlePY shell version a" + str(user["version"]))
                print("------------------------")
                print("What's new: " + user["update_message"])
                if user["update_function"] != False:
                    function = user["update_function"]
                    function()
                    user["update_function"] = False
            else:
                print("There is no update available.")
                
    elif command.startswith("buy ") or command == "buy":
        if not "buy" in user["commands"]:
            print("Invalid command.")
        else:
            commands = command.split(" ")
            commands.append("end")
            commands.append("end")
            if commands[1] == "view":
                subcommand = False
                for entry in software_list:
                    if commands[2] == entry:
                        entry_split = software_list[entry].split("$%")
                        print(str(entry) + ": " + entry_split[0] + " Costs " + entry_split[1] + " points.")
                        subcommand = True
                if subcommand == False:
                    for entry in software_list:
                        entry_split = software_list[entry].split("$%")
                        print(str(entry) + ": " + entry_split[0] + " Costs " + entry_split[1] + " points.")
            else:
                valid_entry = False
                for entry in software_list:
                    if commands[1] == entry:
                        valid_entry = True
                        entry_split = software_list[entry].split("$%")
                        if user["points"] >= int(entry_split[1]):
                            user["points"] -= int(entry_split[1])
                            function = function_list[entry_split[2]]
                            print("Successfully bought {} for {} points.".format(entry, entry_split[1]))
                            entry_split[1] = int(entry_split[1])
                            entry_split[1] *= 1.15
                            entry_split[1] = str(int(entry_split[1]))
                            repeatable = entry_split[3]
                            bought_entry = entry
                            software_list[entry] = "$%".join(entry_split)
                            function()
                        else:
                            print("Insufficient funds.")
                try:
                    if repeatable == "one_time":
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
    elif command.startswith("ls ") or command == "ls":
        if not "ls" in user["commands"]:
            print("Invalid command.")
        else:
            print("game shell home")
           
    elif command.startswith("badd ") or command == "badd":
        if not "badd" in user["commands"]:
            print("Invalid command.")
        else:
            user["points"] += user["point_increment"] * int((1 + random()))
            user["add_command_uses"] += 1
            if user["point_increment"] == 1:
                print("Added " + str(user["point_increment"]) + " point.")
            else:
                print("Added " + str(user["point_increment"]) + " points.")
    elif command.startswith("runpy ") or command == "runpy":
        commands = command.split(" ", 2)
        exec(commands[1])
    else:
        print("Invalid command.")
            
#load game save
try:
    with open('save.json', 'r+') as f:
        data = json.load(f)
    #if the old save doesn't have variables from a newer version, the newer variables won't be deleted
    for variable in data:
        user[variable] = data[variable]
    #load unlocked commands into command list for help command
    if "update" in user["commands"]:
        command_list["update"] = "Updates the system, if there is a new update available."
    if "buy" in user["commands"]:
        command_list["buy"] = "Allows you to buy software to help you get more points. Subcommands: view"
    if "ls" in user["commands"]:
        command_list["ls"] = "Discover what files are on your system so that you can poke around with other software."    
except Exception:
    #if save.json doesn't exist or is empty, skip loading instead of crashing
    pass

print("IdlePY shell version a" + str(user["version"]))
print("------------------------")
time.sleep(1)
while True:
    next_command()

    