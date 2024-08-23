import sys
import os
import time
import importlib.metadata

from textPlay.colors import *


# CONSTANTS
VERSION = 'v0.1.0'
author = 'Rakesh Kanna'
title = f'\n\t{CYAN}PIP CREATOR{RESET} {VERSION}\n'
tic = f"{BOLD}{BRIGHT_GREEN}√{RESET} "

check_directory_err = f"{RED}Files exist in the directory. Try another directory or delete these files.{RESET}"

readme_success = f"{tic}README.md created successfully."
setuppy_success = f"{tic}setup.py created successfully."
setupcfg_success = f"{tic}setup.cfg created successfully."
pyprojecttoml_success = f"{tic}pyproject.toml created successfully."
requirements_success = f"{tic}requirements.txt created successfully."
gitignore_success = f"{tic}.gitignore created successfully."
license_success = f"{tic}License created successfully."


files_success = f"\n{tic}All files created successfully."
ready_to_code = "Your project folder is ready to code."
file_written_check = f"{tic}Files Written successfully."


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

wrt_prog_remd_ovr = f"{tic} README.md written successfully."
wrt_prog_setuppy_ovr = f"{tic}setup.py written successfully."
wrt_prog_setupcfg_ovr = f"{tic}setup.cfg written successfully."
wrt_prog_pyprojecttoml_ovr = f"{tic}pyproject.toml written successfully."
wrt_prog_requirements_ovr = f"{tic}requirements.txt written successfully."
wrt_prog_gitignore_ovr = f"{tic}.gitignore written successfully."
wrt_prog_license_ovr = f"{tic}LICENSE written successfully."

footer = f"{author}\n{CYAN}Happy Coding!{RESET}"

invalid_input = f"{RED}Invalid input. Please enter 'y' or 'n'.{RESET}"
exit_msg = f"{RED}Exiting the program.{RESET}\n"

def lst_file_display(project, setup, test=False):
    if not test:
        lst_file = f'''
{project}/
│
├── {project}/
│   ├── __init__.py
│   └── main.py
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
└── {setup}
'''
    elif test:
        lst_file = f'''
{project}/
│
├── {project}/
│   ├── __init__.py
│   └── main.py
│
├── test/
│   └── test.py
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
└── {setup}
'''

    return lst_file

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



# OPTIONS
def options(proj_name):

    name = True
    while name:
        projname = input(f"{CYAN}Enter project name {RESET}[{proj_name}] ")
        if not projname:
            projname = proj_name
        name = False

    desc = True
    while desc:
        description = input(f"{CYAN}Enter a description for your project {RESET}")
        if not description:
            description = "No description"
        desc = False

    keyw = True
    while keyw:
        keywords = input(f"{CYAN}Enter keywords for your project {RESET}")
        if not keywords:
            keywords = "NoKeywords"
        keyw = False

    auth = True
    while auth:
        author = input(f"{CYAN}Enter author name {RESET}")
        if not author:
            print(f"{RED}Author name cannot be empty.{RESET}")
            continue
        auth = False

    auth_mail = True
    while auth_mail:
        author_mail = input(f"{CYAN}Enter author email {RESET}")
        if not author_mail:
            print(f"{RED}Author email cannot be empty.{RESET}")
            continue
        auth_mail = False

    lic = True
    while lic:
        licence = input(f"{CYAN}Enter license for your project {RESET}[MIT] ")
        if not licence:
            licence = 'MIT'
        lic = False

    dep = True
    while dep:
        dependencies = input(f"{CYAN}Any dependencies for your project {RESET}")
        dep = False

    return projname, description, keywords, author, author_mail, licence, dependencies


# CHECK FOLDER
def check_folder_contents(dir_path, proj_name):
    required_files = ['LICENSE', 'README.md', 'requirements.txt']
    setup_files = ['setup.py', 'pyproject.toml']
    
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
    

# SETUP.PY FILES
def setuppy_writer(description, keywords, author, author_mail, proj_name, licence, dependencies):
    
    entry_points ='{"console_scripts":["'+proj_name+' = '+proj_name+':main"]}'
    
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
    license="{licence}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords={keywords},
    install_requires=
        {dependencies.split()},
    entry_points={entry_points}
)
'''
    return setuppy


# CREATE PYPROJECT.TOML
def get_package_version(package_name):
    try:
        return f"{package_name}>={importlib.metadata.version(package_name)}"
    except importlib.metadata.PackageNotFoundError:
        return f"{package_name}"

# TODO : If One dependency make a error on writting file
def pyprojecttoml_writer(description, keywords, author, author_mail, proj_name, licence, dependencies):
    keywords = keywords.split()
    if not dependencies:
        dependencies = ""
    else:
        dependencies = dependencies.split() 
        dependencies = " ".join(get_package_version(pkg) for pkg in dependencies)
        dependencies = f'dependencies = {dependencies.split(" ")}'
    licence_ = '{text= "'+licence+'"}' # license = {text = "mit"}
    authors = '[{name= "'+author+'", email= "'+author_mail+'"}]'
    # [{ name = "Rakesh Kanna", email = "rakeshkanna0108@gmail.com" }]
    pyprojecttoml = f'''
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{proj_name}"
version = "0.1.0"
description = "{description}"
authors =  {authors}
license = {licence_}
readme = "README.md"
requires-python = ">=3.8"
keywords = {keywords}

{dependencies}

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: {licence} License",
    "Operating System :: OS Independent",
]

[project.scripts]
my_script = "{proj_name}:main"
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
