import subprocess
import os
import sys
import time
import toml
import re

from textPlay.colors import *
from textPlay.backend import backend_suppress
from pipcreator.constants import check_folder_contents
from pipcreator.constants import footer
from pipcreator.constants import exit_msg, invalid_input

def convert(command):
    loop = True
    while loop:
        conform = input(f"Are you sure you want to convert to distribution file? (y/n) [{CYAN}Y{RESET}]: ")
        if conform.lower() == 'y' or conform.lower() == '' or conform.lower() == 'yes':
            try:
                backend_suppress(command)
                print(f"\n{GREEN}√ Files Converted successfully.{RESET}")
            except Exception as e:
                print(f"{RED}Error on converting... {e}{RESET}")

            loop = False
        
        elif conform.lower() == 'n' or conform.lower() == 'no':
            print(f"{RED}{BOLD}\nAborted.{RESET}")
            loop = False

        else:
            print(invalid_input)


def run_setup_command_convert():
    command = "python -m build"

    directory = os.getcwd()
    print(f"Converting files will happen @ {BRIGHT_BLUE}{directory}{RESET}")

    proj_name = os.path.basename(directory)
    print(f"Project name: {BRIGHT_BLUE}{proj_name}{RESET}\n")

    folder_complete, missing_files = check_folder_contents(directory, proj_name)

    if folder_complete == False:
        time.sleep(1.0)
        print("Folder is missing the following required files:")
        for file_name in missing_files:
            print(f"{YELLOW}{file_name}{RESET}")

    elif folder_complete == True:
        time.sleep(1.0)
        print(f"{GREEN}√ Folder contains all required files.{RESET}")
        try:
            if os.path.exists('pyproject.toml'):
                print(f"{GREEN}√ pyproject.toml found.{RESET}")
                loop = True
                while loop:
                    upd_version = input(f"Update version number? (y/n) [{CYAN}Y{RESET}]: ")
                    if upd_version.lower() == 'y' or upd_version == 'yes'  or upd_version == '':
                        update_toml()
                        loop = False

                    elif upd_version.lower() == 'n' or upd_version == 'no':
                        loop = False

                    else:
                        print(invalid_input)
                print(f"\n{GREEN}√ pyproject.toml updated.{RESET}")


            elif os.path.exists('setup.py'):
                print(f"{GREEN}√ setup.py found.{RESET}")
                loop = True
                while loop:
                    upd_version = input(f"Update version number? (y/n) [{CYAN}Y{RESET}]: ")
                    if upd_version.lower() == 'y' or upd_version == 'yes'  or upd_version == '':
                        update_setup()
                        loop = False

                    elif upd_version.lower() == 'n' or upd_version == 'no':
                        loop = False

                    else:
                        print(invalid_input)
                print(f"\n{GREEN}√ setup.py updated.{RESET}")

            else:
                print(f"{RED}Error: setup.py or pyproject.toml not found.{RESET}")
                sys.exit(1)
                
            convert(command)

        except Exception as e:
            print(f"{RED}Error on Converting...\nERROR: {BOLD}{e}{RESET}")

    else: 
        print(f"{RED}Something went wrong. Please try again.{RESET}")

    time.sleep(1.0)
    print(f"\n{footer}")



# UPDATE PYPROJECT.TOML
def read_toml(file_path):
    with open(file_path, 'r') as f:
        return toml.load(f)

def update_version(toml_data, new_version):
    toml_data['project']['version'] = new_version
    return toml_data

def write_toml(file_path, toml_data):
    with open(file_path, 'w') as f:
        toml.dump(toml_data, f)

def update_toml(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    else:
        try:
            data = read_toml(file_path)
            print(f"Current version: {data['project']['version']}")
            new_version = input(f"Enter new version number: ")
            updated_data = update_version(data, new_version)
            write_toml(file_path, updated_data)
            print(f"Updated version: {new_version}")

        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")


# UPDATE SETUP.PY VERSION
def get_current_version(setup_file='setup.py'):
    with open(setup_file, 'r') as file:
        content = file.read()
    match = re.search(r"version=['\"]([^'\"]+)['\"]", content)
    if match:
        return match.group(1)
    else:
        raise ValueError("Version not found in setup.py")

def set_version(new_version, setup_file='setup.py'):
        with open(setup_file, 'r') as file:
            content = file.read()

        # Replace the version number
        content = re.sub(r"version=['\"][^'\"]+['\"]", f"version='{new_version}'", content)

        with open(setup_file, 'w') as file:
            file.write(content)


def update_setup(setup_file='setup.py'):
    if not os.path.exists(setup_file):
        raise FileNotFoundError(f"File not found: {setup_file}")
    else:
        try:
            print(f"Current version: { get_current_version(setup_file)}")
            new_version = input(f"Enter new version number: ")
            set_version(new_version, setup_file)
            print(f"Updated version:  {get_current_version(setup_file)}")
        
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")