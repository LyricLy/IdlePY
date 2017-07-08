user = {
    "points": 0,
    "point_increment": 1,
    "add_command_uses": 0,
    "commands": [],
    "software": [],
    "new_version": False,
    "update_message": "",
    "update_function": "",
    "display_version": [1, 0],
    "total_version": 1
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
    "BetterAdd": 500,
    "PointHack Pro": 300,
    "Basic Bot": 250,
    "vim": 300,
    "cd": 100
}
repeatable = {
    "Python": False,
    "ls": False,
    "PointHack": True,
    "BetterAdd": False,
    "PointHack Pro": True,
    "vim": False,
    "cd": False,
    "Basic Bot": True
}
software_list_temp = {}
# functions for software from the shop that will trigger when software is bought
def python():
    user["software"].append("python")
    software_list_temp["Basic Bot"] = "Runs the add command once every five seconds."
    software_list_temp["BetterAdd"] = "Adds an improved version of the add command, 'badd' with greater stability and point gaining."

def ls():
    user["software"].append("ls")
    user["commands"].append("ls")
    software_list_temp["vim"] = "A text editor that can be used to edit files. Could you possibly spoof some numbers?"
    software_list_temp["cd"] = "A useful tool to move around your system."
    
def point_hack():
    software_list_temp["PointHack Pro"] = "The professional version of PointHack to increase your point multiplier even more."
    user["point_increment"] += 1
    
def point_hack_pro():
    user["point_increment"] += 2
    
def better_add():
    user["software"].append("better_add")
    user["commands"].append("badd")
    
def placeholder():
    print("This is a placeholder message! This item has not been implemented yet.")
    
# functions for updates that trigger when an update completes
def one_dot_one():
    user["commands"].append("buy")

function_list = {
    "Python": python,
    "ls": ls,
    "PointHack": point_hack,
    "BetterAdd": better_add,
    "PointHack Pro": point_hack_pro,
    "cd": placeholder,
    "vim": placeholder,
    "Basic Bot": placeholder
}
  
def new_update(update_message, function=False):
    print("You have a new update available to the operating system!")
    print("Use the 'update' command to update your system.")
    user["new_version"] = True
    user["update_message"] = update_message
    if function is not False:
        user["update_function"] = function