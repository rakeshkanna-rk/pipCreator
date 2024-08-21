import subprocess
import os
import sys
import time

from textPlay.colors import *
from textPlay.backend import backend_suppress
from constants import check_folder_contents
from constants import title, footer
from constants import exit_msg, invalid_input

def convert(command):
    loop = True
    while loop:
        conform = input("Are you sure you want to convert to sdist and bdist? [y/n]: ")
        if conform.lower() == 'y':
            try:
                backend_suppress(command)
                print(f"\n{GREEN}Files Converted successfully. ✔{RESET}")
            except Exception as e:
                print(f"{RED}Error on converting... {e}{RESET}")

            loop = False
        
        elif conform.lower() == 'n':
            print(f"{RED}{BOLD}\nAborted.{RESET}")
            loop = False

        else:
            print(invalid_input)




def run_setup_command_convert():
    command = "python setup.py sdist bdist_wheel"

    print(title)

    directory = os.getcwd()
    print(f"Uploading files will happen in current directory: {YELLOW}{directory}{RESET}")

    proj_name = os.path.basename(directory)
    print(f"Project name: {YELLOW}{proj_name}{RESET}\n")

    folder_complete, missing_files = check_folder_contents(directory, proj_name)

    if folder_complete == False:
        time.sleep(1.0)
        print("Folder is missing the following required files:")
        for file_name in missing_files:
            print(f"{YELLOW}{file_name}{RESET}")

    elif folder_complete == True:
        time.sleep(1.0)
        print(f"{GREEN}Folder contains all required files. ✔{RESET}")
        try:
            convert(command)

        except Exception as e:
            print(f"Error on Converting...\nERROR: {e}")

    else: 
        print(f"{RED}Something went wrong. {exit_msg}{RESET}")

    time.sleep(1.0)
    print(f"\n{footer}")

    
