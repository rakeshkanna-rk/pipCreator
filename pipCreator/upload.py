import os
import subprocess
import time
import sys

from textPlay.colors import *
from textPlay.backend import backend_exec
from pipcreator.constants import check_folder_contents
from pipcreator.constants import footer
from pipcreator.constants import exit_msg, invalid_input


def uploader(command):
    try:
        conform = input(f"{YELLOW}This will use twine to upload the package.{YELLOW} \nAre you sure you want to proceed? (y/n): ")
        loop = True
        while loop:
            if conform.lower() == "y":
                backend_exec(command)
                print(f"{GREEN}\nCommand executed successfully. ✔\n")
                loop = False
                return True

            elif conform.lower() == "n":
                print(f"{RED}\nCommand cancelled. \n")
                loop = False
                return False

            else:
                print(invalid_input)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def check_bsdist(folder_path, required_files):
    
    folder_files = os.listdir(folder_path)

    missing_files = [file_name for file_name in required_files if file_name not in folder_files]

    if not missing_files:
        return True, None
    else:
        return False, missing_files


def run_setup_command_upload():
    command = "twine upload dist/*"

    directory = os.getcwd()
    print(f"Uploading files will happen @ {YELLOW}{directory}{YELLOW}")

    proj_name = os.path.basename(directory)
    print(f"Project name: {YELLOW}{proj_name}{YELLOW}\n")

    print(f"\n{YELLOW}Make sure you have an account and genrated an API key at https://pypi.org{YELLOW}")

    loop = True
    while loop:
        conform = input("Did you convert the files to sdist and bdist? (y/n): ")
        if conform.lower() == 'y':
            loop = False
        
        elif conform.lower() == 'n':
            print(f"USE: {MAGENTA}pipcreator convert{YELLOW}")
            print(f"{RED}\nCommand cancelled.\n{exit_msg}{YELLOW}")
            print(f"\n{footer}")
            loop = False  
            sys.exit()      

        else:
            print(invalid_input)


    folder_complete, missing_files = check_folder_contents(directory, proj_name)


    if folder_complete == False:
        time.sleep(1.0)
        print("Folder is missing the following required files:")
        for file_name in missing_files:
            print(f"{YELLOW}{file_name}{YELLOW}")

    elif folder_complete == True:
        time.sleep(1.0)
        required_files = ['dist', f'{proj_name}.egg-info']
        bsdist_check, missing_files = check_bsdist(directory, required_files)
        if bsdist_check == False:
            print(f"Folder missing the build and dist folders.")
            sys.exit(1)
        print(f"\n{GREEN}Folder contains all required files. ✔{YELLOW}")
        try:
            done = uploader(command)
            if done:
                print(f"{MAGENTA}Twine Operation Completed...{YELLOW}")

        except Exception as e:
            print(f"Error on Uploading...\nERROR: {e}")

    else: 
        print(f"{RED}Something went wrong. Please try again.{YELLOW}")

    time.sleep(1.0)
    print(f"\n{footer}")



