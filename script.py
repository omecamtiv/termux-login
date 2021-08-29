#!/bin/env python3


# Importing packages.


import bcrypt
import os
import signal
import getpass
import argparse
from time import sleep


# Parsing command line arguments.

parser = argparse.ArgumentParser(prog='auth',
        description='Termux Login Utility')
parser.add_argument(
        '-p',
        action='store_true',
        help='change login credentials')

parser.add_argument(
        '-v',
        action='version',
        version='%(prog)s 1.1')

args = parser.parse_args()


# Define color tables.


class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'

    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'

    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'


# Defining variables.


userPrompt = "Username : "
passPrompt = "Password : "
newUserPrompt = "Enter A Username : "
newPassPrompt = "Enter A Password : "
cnfPassPrompt = "Confirm Password : "
loginHeading = "\nLogin to Termux!\n"
registerHeading = "\nRegister to Termux!\n"
changeHeading = "\nVerify Credentials!\n"
successStatus = "\nStatus : Login Successfull."
failedStatus = "\nStatus : Login Failed."
unauthStatus = "\nStatus : Unauthorised."
authStatus = "\nStatus: Authorised."
registeredStatus = "\nStatus: User Registered."
passwdPath = os.path.expandvars('$PREFIX/etc/passwd')
passwdNotFound = "\nError: passwd file not found."
user = ""
hashedPassword = ""


# Check for `passwd` file and retrieve `user` and `hashedPassword`.


isPasswdPresent = os.path.isfile(passwdPath)

if (isPasswdPresent):
    with open(passwdPath, 'r') as passwdFile:
        content = passwdFile.readline().strip()
        if len(content) != 0 or len(content.split(' : ')) != 0:
            user = content.split(' : ')[0]
            hashedPassword = content.split(' : ')[1]
    passwdFile.close()


# Register new user with password.


def register():
    print(colors.fg.lightgrey + colors.bold + colors.underline + registerHeading + colors.reset)
    newUser = ""
    newPass = ""
    cnfPass = ""
    while (newUser == "" or newPass == "" or newPass != cnfPass):
        newUser = input(colors.fg.orange + colors.bold + newUserPrompt + colors.reset)
        newPass = getpass.getpass(colors.fg.orange + colors.bold + newPassPrompt + colors.reset)
        cnfPass = getpass.getpass(colors.fg.orange + colors.bold + cnfPassPrompt + colors.reset)

    passHash = bcrypt.hashpw(newPass.encode('utf-8'), bcrypt.gensalt())
    newHashedPassword = passHash.decode('utf-8')

    passwdContent = "%s : %s" % (newUser, newHashedPassword)

    with open(passwdPath, 'w') as passwdFile:
        passwdFile.write(passwdContent)
    passwdFile.close()

    print(colors.fg.green + colors.bold + colors.underline + registeredStatus + colors.reset)

    return 


# Login existing user.


def login():
    print(colors.fg.lightgrey + colors.bold + colors.underline + loginHeading + colors.reset)
    loginUser = input(colors.fg.orange + colors.bold + userPrompt + colors.reset)
    loginPass = getpass.getpass(colors.fg.orange + colors.bold + passPrompt + colors.reset)

    if (loginUser == user and bcrypt.checkpw(loginPass.encode('utf-8'), hashedPassword.encode('utf-8'))):
        print(colors.fg.green +  colors.bold + colors.underline + successStatus + colors.reset)
    else:
        print(colors.fg.red + colors.bold + colors.underline + failedStatus + colors.reset)
        print("")
        os.kill(os.getppid(), signal.SIGHUP)
    return


# Change credentials.


def change():
    print(colors.fg.lightgrey + colors.bold + colors.underline + changeHeading + colors.reset) 
    loginUser = input(colors.fg.orange + colors.bold + userPrompt + colors.reset)
    loginPass = getpass.getpass(colors.fg.orange + colors.bold + passPrompt + colors.reset)

    if (loginUser == user and bcrypt.checkpw(loginPass.encode('utf-8'), hashedPassword.encode('utf-8'))):
        print(colors.fg.green + colors.bold + colors.underline + authStatus + colors.reset)
        register()
    else:
        print(colors.fg.red + colors.bold + colors.underline + unauthStatus + colors.reset)
    return


# Main Function


os.system('clear')
if (args.p):
    if (user != "" or hashedPassword != ""):
        change()
    else:
        print(colors.fg.red + colors.bold + colors.underline + passwdNotFound + colors.reset)
else:
    if (user != "" or hashedPassword != ""):
        login()
    else:
        register()

sleep(1)
os.system('clear')
