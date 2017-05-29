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
            commands = command.split(" ", 1)
            commands.append("end")
            commands.append("end")
            if commands[1] == "view":
                for entry in software_list:
                    print(entry + ": " + software_list[entry] + " Costs " + software_prices[entry] + " points.")
            else:
                valid_entry = False
                for entry in software_list:
                    if commands[1] == entry:
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
        commands = command.split(" ", 1)
        try:
            exec(commands[1])
        except Exception as error:
            print("Failed to execute code.")
            print(error)
    else:
        print("Invalid command.")