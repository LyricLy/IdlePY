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
    "Python": "A useful programming language that can allow you to program other software.",
    "ls": "Discover what files are on your system so that you can poke around with other software.",
    "PointHack": "Get more points with the 'add' command!"
}
software_prices = {
    "Python": 1000,
    "ls": 700,
    "PointHack": 50,
    "BetterAdd": 500
}
repeatable = {
    "Python": False,
    "ls": False,
    "PointHack": True,
    "BetterAdd": False
}
software_list_temp = {}
#functions for software from the shop that will trigger when software is bought
def python():
    user["software"].append("python")
    software_list_temp["Basic Bot"] = "Runs the add command once every five seconds."
    software_list_temp["BetterAdd"] = "Adds an improved version of the add command, 'badd' with greater stability and point gaining."

def ls():
    user["software"].append("ls")
    user["commands"].append("ls")
    software_list_temp["vim"] = "A text editor that can be used to edit files. Could you possibly spoof some numbers?"
    software_list_temp["cd"] = "A useful tool to move around your system.$%300$%cd$%one_time"
    
def point_hack():
    software_list_temp["PointHack Pro"] = "The professional version of PointHack to increase your point multiplier even more."
    user["point_increment"] += 1
    
def better_add():
    user["software"].append("better_add")
    user["commands"].append("badd")
#functions for updates that trigger when an update completes
def one_dot_one():
    user["commands"].append("buy")
    command_list["buy"] = "Allows you to buy software to help you get more points. Subcommands: view"

function_list = {
    "Python": python,
    "ls": ls,
    "PointHack": point_hack,
    "BetterAdd": better_add
}
  
def new_update(update_message, function=False):
    print("You have a new update available to the operating system!")
    print("Use the 'update' command to update your system.")
    user["new_version"] = True
    user["update_message"] = update_message
    if function != False:
        user["update_function"] = function