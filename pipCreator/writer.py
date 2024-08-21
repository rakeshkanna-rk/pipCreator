# TODO : Correct All Funtion and ERRORS

import os
import sys
import time
from string import ascii_lowercase, ascii_uppercase, digits

from textPlay.colors import *
from textPlay.files import write_file, list_dir

# CONSTANTS
from pipcreator.constants import *


# CHECK DIRECTORY
def check_directory(directory, proj_name):

    # Check if directory exists
    if not os.path.exists(directory):
        # options()
        print(f"{YELLOW}Directory doesn't exist.{RESET}")

        dir_loop = True
        while dir_loop:
            dir_crt = input(f"Do you like to create the directory? (y/n) [{CYAN}Y{RESET}/{RED}N{RESET}] ")
            if dir_crt.lower() == 'y' or dir_crt.lower() == '':
                os.makedirs(directory)
                print(f"{GREEN}√ Directory created successfully.{RESET}")
                time.sleep(0.5)
                description, keywords, author, author_mail, licence, dependencies = options()
                create_files_and_folders(directory, description, keywords, author, author_mail, proj_name, licence, dependencies)
                dir_loop = False

            elif dir_crt.lower() == 'n':
                print(f"{RED}Creating project aborted.{RESET}")
                print(f"\n{footer}")
                sys.exit(1)

            else:
                print(invalid_input)

    else:
        # Check if directory is empty
        if not os.listdir(directory):
            description, keywords, author, author_mail, licence, dependencies = options()
            print("Creating files and folders...", end="\r")
            time.sleep(1.0)
            create_files_and_folders(directory, description, keywords, author, author_mail, proj_name, licence, dependencies)
        else:
            print(check_directory_err)
            list_dir(directory)


# CREATE README.MD
def create_readme(directory, description, proj_name):
    # Create README.md
    with open(os.path.join(directory, 'README.md'), 'w') as f:
        readme = f'''
# {proj_name}
{description}
'''
        f.write(readme)
    print(readme_success)
    return readme


# CREATE SETUP.PY
def create_setuppy(directory, description, keywords, author, author_mail, proj_name, licence="MIT"):
    keywords = keywords.split()

    with open(os.path.join(directory, 'setup.py'), 'w') as f:
        setuppy = setuppy_writer(description, keywords, author, author_mail, proj_name, licence)
        f.write(setuppy)
    print(setuppy_success)
    return setuppy


# CREATE SETUP.CFG
def create_setupcfg(directory, description, keywords, author, author_mail, proj_name, licence="MIT"):
    with open(os.path.join(directory, 'setup.cfg'), 'w') as f:
        setupcfg = setupcfg_writer(description, keywords, author, author_mail, proj_name, licence)
        f.write(setupcfg)
    print(setupcfg_success)
    return setupcfg


# CREATE PYPROJECT.TOML
def create_pyprojecttoml(directory, description, keywords, author, author_mail, proj_name, licence="MIT"):
    with open(os.path.join(directory, 'pyproject.toml'), 'w') as f:
        pyprojecttoml = pyprojecttoml_writer(description, keywords, author, author_mail, proj_name, licence)
        f.write(pyprojecttoml)
    print(pyprojecttoml_success)
    return pyprojecttoml


# CREATE REQUIREMENTS.TXT
def create_requirements(directory, requirements):
    requirements = requirements.split()
    with open(os.path.join(directory, 'requirements.txt'), 'w') as f:
        for dependency in requirements:
            f.write(f"{dependency}\n")
    print(requirements_success)
    return requirements


# .GITIGNORE
def create_gitignore(directory):
    with open(os.path.join(directory, '.gitignore'), 'w') as f:
        f.write(gitignore)
    print(gitignore_success)
    return gitignore


# LICENSE
def create_license(directory):
    with open(os.path.join(directory, 'LICENSE'), 'w') as f:
        license = '# your license here\n'
        f.write(license)
    print(license_success)
    return license


# FOLDERS
def folders(directory, proj_name, folder_name):
    os.makedirs(os.path.join(directory, folder_name))
    with open(os.path.join(directory, folder_name, '__init__.py'), 'w') as f:
        init = init_writer()
        f.write(init)
        print(f" {GREEN}√ {proj_name}/__init__.py created successfully.{RESET}")
        time.sleep(0.5)

    with open(os.path.join(directory, folder_name, 'main.py'), 'w') as f:
        main = main_writer()
        f.write(main)
        print(f"{GREEN}√ {proj_name}/main.py created successfully.{RESET}\n")
        time.sleep(0.5)

    return init, main

# CREATE FILES AND FOLDERS
def create_files_and_folders(directory, description, keywords, author, author_mail, proj_name, licence="MIT", dependencies=""): 

    print(f"Setup Types: {BOLD}{GREEN}setup.py {YELLOW}pyproject.toml{RESET}")
    setup = ""
    loop = True
    while loop:
        setuppy = input(f"Do you want to create a setup.py file for your project? (y/n) [{CYAN}Y{RESET}] ")
        if setuppy.lower() == 'y' or setuppy.lower() == 'yes' or setuppy.lower() == '':
            setuppy = create_setuppy(directory, description, keywords, author, author_mail, proj_name, licence)
            time.sleep(0.5)
            setup = "setup.py"
            break
        
        pyproj = input(f"Do you want to create a pyproject.toml file for your project? (y/n) [{CYAN}Y{RESET}]")
        if pyproj.lower() == 'y' or pyproj.lower() == 'yes' or pyproj.lower() == '':
            # Create files
            pyproj = create_pyprojecttoml(directory, description, keywords, author, author_mail, proj_name, licence)
            time.sleep(0.5)
            setup = "pyproject.toml"
            break

    if not setuppy and not pyproj:
        print(f"{YELLOW}No setup file created{RESET}\nDefaulting to pyproject.toml\n")
        pyproj = create_pyprojecttoml(directory, description, keywords, author, author_mail, proj_name, licence)

    readme = create_readme(directory, description, proj_name)
    time.sleep(0.5)
    gitignore_fh = create_gitignore(directory)
    time.sleep(0.5)
    licence = create_license(directory)
    time.sleep(0.5)
    requirements = create_requirements(directory, dependencies)
    time.sleep(0.5)

    # Folder name
    folder_name = os.path.basename(directory)
    # CREATING FOLDERS
    init, main = folders(directory, proj_name, folder_name)

    print(lst_file_display(proj_name, setup))

    print(f"{files_success}\n{ready_to_code}")
    print(f"\n\t {BRIGHT_BLUE}cd{RESET} {directory}\n")
    print(footer)


# MAIN (PIP CREATOR)
def pip_creator():

    if len(sys.argv) != 3:
        print("Usage: pipcreator create <directory>")
        sys.exit(1)

    folder_name = ascii_lowercase + ascii_uppercase + digits + '_./'

    directory = sys.argv[2]

    if "-" in directory:
        print(f"{YELLOW}The ' - ' will be replaced as '_' in the folder name{RESET}")
        directory = directory.replace("-", "_")

    if any(char not in folder_name for char in directory):
        print(f"{RED}Invalid directory name{RESET}")
        print(f"{YELLOW}Directory name must contain only the following characters:{RESET}")
        print("A-Z a-z 0-9 _ \n")
        print(footer)
        sys.exit(1)

    if directory == '.' or directory == './':
        directory = os.getcwd()

    proj_name = os.path.basename(directory)

    print(f'Creating project @ {directory}')

    check_directory(directory, proj_name)

