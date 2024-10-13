import sys
import os
import time
import importlib.metadata

from textPlay.colors import *

from pipcreator.package import check_requirements, update_setup, update_toml 

# CONSTANTS
VERSION = 'v0.1.0'
author = 'Rakesh Kanna'
title = f'\n\t{CYAN}PIP CREATOR{RESET} {VERSION}\n'
tic = f"{BOLD}{BRIGHT_GREEN}√{RESET} "

check_directory_err = f"{RED}Files exist in the directory. Try another directory or delete following files.{RESET}"

readme_success = f"{tic}README.md created successfully."
setuppy_success = f"{tic}setup.py created successfully."
setupcfg_success = f"{tic}setup.cfg created successfully."
pyprojecttoml_success = f"{tic}pyproject.toml created successfully."
requirements_success = f"{tic}requirements.txt created successfully."
gitignore_success = f"{tic}.gitignore created successfully."
license_success = f"{tic}License created successfully."


files_success = f"\n{tic}All files created successfully."
ready_to_code = "\nYour project folder is ready to code."
file_written_check = f"{tic}Files Written successfully."

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
error = f"{BOLD}{RED}Errors: {RESET}"
error_msg = f"{BOLD}{RED}Error: {RESET}"
warn = f"{BOLD}{YELLOW}Warnings: {RESET}"



# CREATE TEMPLATE FILES ===================================================================

def lst_file_display(project, setup, test=False):
    if not test:
        lst_file = f'''
{BOLD}Project Structure{RESET}
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



# UPDATING FILES =============================================================


def update_dependencies(installed , already_installed):
    upd_req = input(f"\nDo you want to update requirements.txt? (y/n) [{CYAN}Y{RESET}] ")
    if not upd_req:
        upd_req = 'y'
    if upd_req.lower() == 'y':
        content = check_requirements(installed_now = installed + already_installed)

    

    if os.path.exists("pyproject.toml"):
        print(f"{GREEN}Found pyproject.toml.{RESET}")
        upd_setup = input(f"Do you want to update pyproject.toml? (y/n) [{CYAN}Y{RESET}] ")
        if not upd_setup:
            upd_setup = 'y'
        if upd_setup.lower() == 'y':
            update_toml(file_path='pyproject.toml', dependencies_to_add=content)

    elif os.path.exists("setup.py"):
        print(f"{GREEN}Found setup.py.{RESET}")
        upd_setup = input(f"Do you want to update setup.py? (y/n) [{CYAN}Y{RESET}] ")
        if not upd_setup:
            upd_setup = 'y'
        if upd_setup.lower() == 'y':
            update_setup(setup_file='setup.py', new_dependencies=content)

    else:
        print(f"{RED}Error: setup.py or pyproject.toml not found.{RESET}")




# LOADING =====================================================================================
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








import subprocess
import sys

def get_installed_version(package_name):
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "show", package_name],
            capture_output=True,
            text=True,
            check=True
        )
        for line in result.stdout.splitlines():
            if line.startswith("Version:"):
                return line.split()[1]
    except subprocess.CalledProcessError:
        return None

def get_latest_version(package_name):
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "index", "versions", package_name],
            capture_output=True,
            text=True,
            check=True
        )
        versions = []
        for line in result.stdout.splitlines():
            if line.startswith("Available versions:"):
                versions = line.split(":")[1].strip().split(", ")
                break
        if versions:
            return versions[0]
        return None
    except subprocess.CalledProcessError:
        return None

def check_package_latest(package_name):
    installed_version = get_installed_version(package_name)
    latest_version = get_latest_version(package_name)

    if installed_version and latest_version:
        if installed_version == latest_version:
            return 
        else:
            return f"{YELLOW}{package_name} is not up to date.{RESET} \nInstalled version: {installed_version}, \nLatest version: {latest_version}. \nUse {MAGENTA}pipc update {package_name}'{RESET} to update."
    else:
        return f"{package_name} is not installed."



import importlib.util

def is_package_installed(package_name):
    package_spec = importlib.util.find_spec(package_name)
    return package_spec is not None

# Example usage
# package_name = "requests"
# if is_package_installed(package_name):
#     print(f"The package '{package_name}' is installed.")
# else:
#     print(f"The package '{package_name}' is not installed.")

