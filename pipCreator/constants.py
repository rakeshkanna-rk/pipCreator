import sys
import os
import time

from textPlay.colors import *


# CONSTANTS
VERSION = 'v0.1.0'
author = 'Rakesh Kanna'
title = f'\n\t{CYAN}PIP CREATOR{RESET} {VERSION}\n'

check_directory_err = f"{RED}Files exist in the directory. Try another directory or delete these files.{RESET}"

readme_success = f"{GREEN}README.md created successfully. ✔{RESET}"
setuppy_success = f"{GREEN}setup.py created successfully. ✔{RESET}"
setupcfg_success = f"{GREEN}setup.cfg created successfully. ✔{RESET}"
pyprojecttoml_success = f"{GREEN}pyproject.toml created successfully. ✔{RESET}"
requirements_success = f"{GREEN}requirements.txt created successfully. ✔{RESET}"
gitignore_success = f"{GREEN}.gitignore created successfully. ✔{RESET}"
license_success = f"{GREEN}License created successfully. ✔{RESET}"


files_success = f"\n{GREEN}All files created successfully. ✔{RESET}"
ready_to_code = "Your project folder is ready to use."
file_written_check = f"{GREEN}Files Written successfully. ✔{RESET}"


crtfd_msg = "Creating folder... → "
crtfd_msg_ovr = f"{GREEN}Folder created successfully. ✔ → "
crtfl_msg = "Creating files... → "
crtfl_msg_ovr = f"{GREEN}Files created successfully. ✔ → "
wrtfl_msg = "Writing files... → "
wrtfl_msg_ovr = f"{GREEN}Files written successfully. ✔ → "
test_end_msg = f"\r{GREEN}Test Folder has been created successfully! ✔{RESET}\n"


wrt_prog_remd = "Writing README.md files... → "
wrt_prog_setuppy = "Writing setup.py files... → "
wrt_prog_setupcfg = "Writing setup.cfg files... → "
wrt_prog_pyprojecttoml = "Writing pyproject.toml files... → "
wrt_prog_requirements = "Writing requirements.txt files... → "
wrt_prog_gitignore = "Writing .gitignore files... → "
wrt_prog_license = "Writing LICENSE files... → "

wrt_prog_remd_ovr = f"{GREEN}README.md written successfully. ✔{RESET}"
wrt_prog_setuppy_ovr = f"{GREEN}setup.py written successfully. ✔{RESET}"
wrt_prog_setupcfg_ovr = f"{GREEN}setup.cfg written successfully. ✔{RESET}"
wrt_prog_pyprojecttoml_ovr = f"{GREEN}pyproject.toml written successfully. ✔{RESET}"
wrt_prog_requirements_ovr = f"{GREEN}requirements.txt written successfully. ✔{RESET}"
wrt_prog_gitignore_ovr = f"{GREEN}.gitignore written successfully. ✔{RESET}"
wrt_prog_license_ovr = f"{GREEN}LICENSE written successfully. ✔{RESET}"

footer = f"{author}\n{CYAN}Happy Coding!{RESET}"

invalid_input = f"{RED}Invalid input. Please enter 'y' or 'n'.{RESET}"
exit_msg = f"{RED}Exiting the program.{RESET}\n"


gitignore = '''
# Byte-compiled / optimized Python files
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environment
venv/
env/
*.env

# Compiled files
*.o
*.class
*.dll
*.exe

# Temporary files
*~
*.swp
*.log

# Miscellaneous
.DS_Store
.idea/
.vscode/
'''

# PROGRESS BAR
def progress_bar(progress, length=50, symbol='█', empty_symbol='-', color_on_completion=GREEN):
    filled_length = int(length * progress)
    bar = symbol * filled_length + empty_symbol * (length - filled_length)
    color = color_on_completion if progress == 1 else ''
    print(f'|{color}{bar}{RESET}| {progress:.1%}', end='\r')


def erase_bar(progress, length=50, symbol='█', empty_symbol='-', messages=None):
    messages = messages or []
    filled_length = int(length * progress)
    bar = symbol * filled_length + empty_symbol * (length - filled_length)
    
    if progress == 1:
        time.sleep(0.5)
        sys.stdout.write(f'\r{" " * (length + len(messages[-1]) + 10)}\r')
        sys.stdout.write(RESET)
        sys.stdout.flush()

    elif progress == 0.98:
        sys.stdout.write(GREEN)
        sys.stdout.write(f'\r{" " * (length + len(messages[-1]) + 10)}')
        
    else:
        # Determine the current message index based on the progress
        message_index = min(int(progress * len(messages) * 2), len(messages) - 1)
        current_message = messages[message_index]
        
        sys.stdout.write(f'\r|{bar}| {progress:.0%} {current_message}')
        sys.stdout.flush()



#
def options():
    desc = True
    while desc:
        description = input(f"{CYAN}Enter a description for your project: {RESET}")
        desc = False

    keyw = True
    while keyw:
        keywords = input(f"{CYAN}Enter keywords for your project: {RESET}")
        keyw = False

    auth = True
    while auth:
        author = input(f"{CYAN}Enter author name: {RESET}")
        auth = False

    auth_mail = True
    while auth_mail:
        author_mail = input(f"{CYAN}Enter author email: {RESET}")
        auth_mail = False

    lic = True
    while lic:
        licence = input(f"{CYAN}Enter license for your project: {RESET}")
        lic = False

    return description, keywords, author, author_mail, licence


def check_folder_contents(dir_path, proj_name):
    required_files = [proj_name, '.gitignore', 'LICENSE', 'README.md', 'requirements.txt']
    setup_files = ['setup.py', 'setup.cfg', 'pyproject.toml']
    
    folder_files = os.listdir(dir_path)
    
    # Check for required files
    missing_files = [file_name for file_name in required_files if file_name not in folder_files]
    
    # Check if at least one setup file is present
    setup_present = any(file_name in folder_files for file_name in setup_files)
    
    if not missing_files and setup_present:
        return True, None
    else:
        if not setup_present:
            missing_files.append("At least one setup file needed")
        return False, missing_files


def file_printer(readme, setuppy, setupcfg, pyprojecttoml, requirements, gitignore_fh, init, main, proj_name):
    print(f'''
--------------------------------
README.md
{readme}
--------------------------------

--------------------------------
setup.py
{setuppy}
--------------------------------

--------------------------------
setup.cfg
{setupcfg}
--------------------------------

--------------------------------
pyproject.toml
{pyprojecttoml}
--------------------------------

--------------------------------
requirements.txt
{requirements}

--------------------------------
.gitignore
{gitignore_fh}
--------------------------------

--------------------------------
{proj_name}/__init__.py
{init} 
--------------------------------

--------------------------------
{proj_name}/main.py
{main}
--------------------------------
''')
    


def setuppy_writer(description, keywords, author, author_mail, proj_name, licence):
    setuppy = f'''
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="{proj_name}",
    version="0.1.0",
    description="{description}",
    author="{author}",
    author_email='{author_mail}',
    licence="{licence}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords={keywords},
)
'''
    return setuppy

def setupcfg_writer(description, keywords, author, author_mail, proj_name, licence):
    keywords = ', '.join(keywords.split())
    setupcfg = f'''
[metadata]
name = {proj_name}
version = 0.1.0
description = {description}
author = {author}
author_email = {author_mail}
license = {licence}
keywords = {keywords}

[options]
packages = find:
python_requires = >=3.6
'''
    return setupcfg

def pyprojecttoml_writer(description, keywords, author, author_mail, proj_name, licence):
    keywords = keywords.split()
    pyprojecttoml = f'''
[tool.poetry]
name = "{proj_name}"
version = "0.1.0"
description = "{description}"
author = "{author}"
author_email = "{author_mail}"
license = "{licence}"
keywords = {keywords}
[tool.poetry.dependencies]
python = ">=3.6"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
'''

    return pyprojecttoml


# FOLDERS
def init_writer():
    init = f'''
from .main import main

__all__ = ["main"]
'''
    return init

def main_writer():
    main = f'''
def main():
    print("Hello, World!")
'''
    return main


# test/test.py
def test_writer(proj_name):
    test = f'''
import unittest
from {proj_name} import hello 

# Define a test class
class TestHelloFunction(unittest.TestCase):

    # Define a test method to test hello() function
    def test_hello(self):
        # Call the hello() function
        result = hello()

        # Assert the result
        self.assertEqual(result, "Hello, World!")

if __name__ == '__main__':
    unittest.main()

'''
    return test

def test_show_writer(proj_name):
    test_show =f'''
--------------------------------
test/test.py
--------------------------------
import unittest
from {proj_name} import hello 

# Define a test class
class TestHelloFunction(unittest.TestCase):

    def test_hello(self):
        # Call the hello() function
        result = hello()

        # Assert the result
        self.assertEqual(result, "Hello, World!")

if __name__ == '__main__':
    unittest.main()
--------------------------------
'''
    return test_show