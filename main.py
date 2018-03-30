import time
import json
import base64
import commands_logic
from setup import *

# load game save
try:
    with open('save.json', 'r+') as f:
        data = json.loads(base64.b64decode(f.read().encode('utf-8')).decode('utf-8'))
    # if the old save doesn't have variables from a newer version, the newer variables won't be deleted
    for variable in data["user"]:
        user[variable] = data["user"][variable]
    for variable in data["software_prices"]:
        software_prices[variable] = data["software_prices"][variable]
    software_list.clear()
    for variable in data["software_list"]:
        software_list[variable] = data["software_list"][variable]
except (FileNotFoundError, json.JSONDecodeError):
    # if save.json doesn't exist or is empty
    pass
    
print("IdlePY shell version a{}.{}".format(str(user["display_version"][0]), str(user["display_version"][1])))
print("------------------------")
time.sleep(1)
while True:
    commands_logic.next_command()

    