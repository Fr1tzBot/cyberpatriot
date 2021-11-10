import os
import json
from typing import Tuple
import colorama

#Color Functions
def error(message: str) -> None:
    print(colorama.Fore.RED + message + colorama.Style.RESET_ALL)
def warn(message: str) -> None:
    print(colorama.Fore.YELLOW + message + colorama.Style.RESET_ALL)
def success(message: str) -> None:
    print(colorama.Fore.GREEN + message + colorama.Style.RESET_ALL)

adminList = ["admin", "a", "administrator", "root", "big man"]
yesList = ["y", "yes", "ye", "yse", "si", "not no"]
users = {}

prefix = input("enter home dir prefix (/home/): ")
prefix = "/home/" if prefix == "" else prefix

while True:
    user = input("input user: ")
    if user == "":
        break

    userperm = input("input (a)dministrator or (s)tandard: ").lower().strip() in adminList

    if not os.path.exists(prefix + user):
        warn("WARN: user home directory " + prefix + user + " does not exist")

    users[user] = {
        "admin": userperm,
        "homedir": (prefix + user)
    }
for i in users.keys():
    print(i + ": " + str(users[i]))

if not input("Does the above information look correct? ") in yesList:
    exit(1)



#for usr in os.listdir("/home/"):
#    if usr not in usrslst:
#        os.system(f"sudo userdel -r {usr}")
