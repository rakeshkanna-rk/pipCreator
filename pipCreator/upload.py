import os
import subprocess
import time
import sys

from textPlay.colors import *
from textPlay.backend import backend_exec
from pipcreator.constants import check_folder_contents
from pipcreator.constants import footer, tic
from pipcreator.constants import exit_msg, invalid_input

def uploader(command):
    try:
        conform = input(f"{YELLOW}This will use twine to upload the package.{YELLOW} \nAre you sure you want to proceed? (y/n): ")
        loop = True
        while loop:
            if conform.lower() == "y":
                # Execute the command and capture the output
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                # Check for successful upload message in the output
                if "Uploading distributions" in result.stdout and "100%" in result.stdout:
                    print(f"\n{GREEN}{tic}{RESET} Package uploaded successfully.\n")
                else:
                    print(f"\n{RED}Failed to upload the package. Please check the output for errors.\n")

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
    print(f"Uploading files will happen @ {BLUE}{directory}{RESET}")

    proj_name = os.path.basename(directory)
    print(f"Project name: {YELLOW}{proj_name}{RESET}\n")

    print(f"\n{YELLOW}Make sure you have an account and generated an API key at {BLUE}https://pypi.org{RESET}")

    folder_complete, missing_files = check_folder_contents(directory, proj_name)

    if folder_complete == False:
        time.sleep(1.0)
        print("Folder is missing the following required files:")
        for file_name in missing_files:
            print(f"{YELLOW}{file_name}{RESET}")

    elif folder_complete == True:
        time.sleep(1.0)
        required_files = ['dist', f'{proj_name}.egg-info']
        bsdist_check, missing_files = check_bsdist(directory, required_files)
        if bsdist_check == False:
            print(f"Folder missing the build and dist folders.")
            sys.exit(1)
        print(f"\n{GREEN}Folder contains all required files. ✔{RESET}")
        try:
            done = uploader(command)
            if done:
                                print(f"{MAGENTA}Twine Operation Completed...{RESET}")

        except Exception as e:
            print(f"{RED}Error on Uploading...\nERROR: {e}{RESET}")

    else:
        print(f"{RED}Something went wrong. Please try again.{YELLOW}")

    time.sleep(1.0)
    print(f"\n{footer}")


