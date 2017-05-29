import sys
import json
import time
from random import random
import commands
import variable_setup
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

    