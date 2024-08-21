import os
import sys
import time

from textPlay.colors import *
from textPlay.files import read_file
from constants import title, footer
from constants import test_end_msg , crtfd_msg, crtfl_msg, wrtfl_msg, wrtfl_msg_ovr, crtfd_msg_ovr, crtfl_msg_ovr
from constants import test_writer, test_show_writer
from constants import erase_bar
from constants import check_folder_contents


def create_test_folder(proj_name, folder_name):
    os.makedirs(folder_name, exist_ok=True)
    with open(os.path.join(folder_name, 'test.py'), 'w') as f:
        test = test_writer(proj_name)
        f.write(test)

    return test


def test_folder():
    print(title)
    directory = os.getcwd()
    print(f"Test folder will be created in current directory: {YELLOW}{directory}{RESET}")

    proj_name = os.path.basename(directory)
    print(f"Project name: {YELLOW}{proj_name}{RESET}\n")

    print(f"{CYAN}Checking folder contents...{RESET}", end="\r")

    folder_complete, missing_files = check_folder_contents(directory, proj_name)

    if folder_complete == False:
        print("Folder is missing the following required files:")
        for file_name in missing_files:
            print(f"{YELLOW}{file_name}{RESET}")
        time.sleep(1.0)
        print(f"\n{footer}")
        sys.exit(1)

        


    folder_path = 'test'
    if os.path.exists(folder_path):
        time.sleep(0.5)
        print(f"{GREEN}Folder contains all required files. ✔{RESET}")
        print(f"{RED}The folder '{proj_name}/{folder_path}' exists.{RESET}")
    else:
        print(f"{GREEN}Folder contains all required files. ✔{RESET}")
        print(f"The folder '{proj_name}/{folder_path}' does not exist.", end="\r")

        create_test_folder(proj_name, "test")
        print(f"{GREEN}{proj_name}/test.py created successfully. ✔{RESET}")

        time.sleep(0.5)
        print(test_end_msg)

        test_loop = True
        while test_loop:
            check_test = input("Do you want to check the test folder? (y/n): ")
            if check_test.lower() == 'y':
                try:
                    test_show = read_file('test/test.py')
                    print(test_show)
                    test_loop = False
                except FileNotFoundError:
                    print(f"{RED}Error: test/test.py not found.{RESET}")
                    print(f"Use {BOLD}pipcreator create-test{RESET} to create the test folder.")
                    test_loop = False

            elif check_test.lower() == 'n':
                test_loop = False

            else:
                print("Invalid input. Please enter 'y' or 'n'.")


    time.sleep(1.0)
    print(f"\n{footer}")


