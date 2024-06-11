import os

for file in os.listdir("commands"):
    if file.endswith(".py") and file != "__init__.py":
        exec("from commands.{} import *".format(file.rsplit(".",1)[0]))
