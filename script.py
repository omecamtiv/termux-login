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
        version='%(prog)s 1.0')

args = parser.parse_args()


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
    print(registerHeading)
    newUser = ""
    newPass = ""
    cnfPass = ""
    while (newUser == "" or newPass == "" or newPass != cnfPass):
        newUser = input(newUserPrompt)
        newPass = getpass.getpass(newPassPrompt)
        cnfPass = getpass.getpass(cnfPassPrompt)

    passHash = bcrypt.hashpw(newPass.encode('utf-8'), bcrypt.gensalt())
    newHashedPassword = passHash.decode('utf-8')

    passwdContent = "%s : %s" % (newUser, newHashedPassword)

    with open(passwdPath, 'w') as passwdFile:
        passwdFile.write(passwdContent)
    passwdFile.close()

    return 


# Login existing user.


def login():
    print(loginHeading)
    loginUser = input(userPrompt)
    loginPass = getpass.getpass(passPrompt)

    if (loginUser == user and bcrypt.checkpw(loginPass.encode('utf-8'), hashedPassword.encode('utf-8'))):
        print(successStatus)
    else:
        print(failedStatus)
        print("")
        os.kill(os.getppid(), signal.SIGHUP)
    return


# Change credentials.


def change():
    print(changeHeading) 
    loginUser = input(userPrompt)
    loginPass = getpass.getpass(passPrompt)

    if (loginUser == user and bcrypt.checkpw(loginPass.encode('utf-8'), hashedPassword.encode('utf-8'))):
        print(authStatus)
        register()
    else:
        print(unauthStatus)
    return


# Main Function


os.system('clear')
if (args.p):
    if (user != "" or hashedPassword != ""):
        change()
    else:
        print(passwdNotFound)
else:
    if (user != "" or hashedPassword != ""):
        login()
    else:
        register()

sleep(1)
os.system('clear')
