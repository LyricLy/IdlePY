import time
from commands import *
from setup import *

#load game save
try:
    with open('save.json', 'r+') as f:
        data = json.load(f)
    #if the old save doesn't have variables from a newer version, the newer variables won't be deleted
    try:
        for variable in data["user"]:
            user[variable] = data["user"][variable]
        for variable in data["software_prices"]:
            software_prices[variable] = data["software_prices"][variable]
    except KeyError:
        #old save
        for variable in data:
            user[variable] = data[variable]
    #load unlocked commands into command list for help command
    if "update" in user["commands"]:
        command_list["update"] = "Updates the system, if there is a new update available."
    if "buy" in user["commands"]:
        command_list["buy"] = "Allows you to buy software to help you get more points."
    if "ls" in user["commands"]:
        command_list["ls"] = "Discover what files are on your system so that you can poke around with other software."    
except (FileNotFoundError, json.JSONDecodeError):
    #if save.json doesn't exist or is empty
    pass

print("IdlePY shell version a{}.{}".format(str(user["display_version"][0]), str(user["display_version"][1])))
print("------------------------")
time.sleep(1)
while True:
    next_command()

    