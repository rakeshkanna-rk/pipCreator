import os
import sys
import time
from string import ascii_lowercase, ascii_uppercase, digits

from textPlay.colors import *
from textPlay.files import write_file, list_dir

# CONSTANTS
from pipcreator.constants import *





#==============================================================================================

# WRITERS

# CREATE README.MD
def create_readme(directory, description, proj_name):
    # Create README.md
    with open(os.path.join(directory, 'README.md'), 'w') as f:
        readme = f'''# {proj_name}  
{description}
'''
        f.write(readme)
    print(readme_success)
    return readme


# CREATE SETUP.PY
def create_setuppy(directory, description, keywords, author, author_mail, proj_name, licence, dependencies):
    keywords = keywords.split()

    with open(os.path.join(directory, 'setup.py'), 'w') as f:
        setuppy = setuppy_writer(description, keywords, author, author_mail, proj_name, licence, dependencies)
        f.write(setuppy)
    print(setuppy_success)
    return setuppy


# CREATE PYPROJECT.TOML
def create_pyprojecttoml(
        directory, description, keywords, 
        author, author_mail, proj_name, licence, dependencies):
    with open(os.path.join(directory, 'pyproject.toml'), 'w') as f:
        pyprojecttoml = pyprojecttoml_writer(description, keywords, author, author_mail, proj_name, licence, dependencies)
        f.write(pyprojecttoml)
    print(pyprojecttoml_success)
    return pyprojecttoml


# CREATE REQUIREMENTS.TXT
def create_requirements(directory, requirements: str):
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
        print(f"{tic}{proj_name}/__init__.py created successfully.{RESET}")
        time.sleep(0.5)

    with open(os.path.join(directory, folder_name, 'main.py'), 'w') as f:
        main = main_writer()
        f.write(main)
        print(f"{tic}{proj_name}/main.py created successfully.{RESET}")
        time.sleep(0.5)

    return init, main

#=============================================================================================




# CREATE FILES AND FOLDERS
def create_files_and_folders(directory, description, keywords, author, author_mail, proj_name, licence, dependencies): 

    # TEST
    test = input(f"\nDo you want to create a test folder? (y/n) [{CYAN}Y{RESET}] ")
    if not test:
        test = "Y"

    # INIT GIT
    git = input(f"Do you want to initialize git? (y/n) [{CYAN}Y{RESET}] ")
    if not git:
        git = "Y"

    if git.lower() == 'y' or git.lower() == 'yes':
        from  textPlay import backend_exec 
        try:
            backend_exec("git init")
        except Exception as e:
            print(f"{BOLD}{RED}Error: {e}{RESET}")

    # SETUP TYPE
    print(f"\nSetup Types: {BOLD}{GREEN}setup.py {YELLOW}pyproject.toml{RESET}")
    setup = ""
    loop = True
    count = 0
    while loop:
        setuppy = input(f"{GREEN}●{RESET} Do you want to create a setup.py file for your project? (y/n) ")
        count += 1
        if setuppy.lower() == 'y' or setuppy.lower() == 'yes':
            print()
            setuppy = create_setuppy(directory, description, keywords, author, author_mail, proj_name, licence, dependencies)
            time.sleep(0.5)
            setup = "setup.py"
            break
        
        pyproj = input(f"{YELLOW}●{RESET} Do you want to create a pyproject.toml file for your project? (y/n) ")
        count += 1
        if pyproj.lower() == 'y' or pyproj.lower() == 'yes':
            print()
            pyproj = create_pyprojecttoml(directory, description, keywords, author, author_mail, proj_name, licence, dependencies)
            time.sleep(0.5)
            setup = "pyproject.toml"
            break

        if count == 8:
            print("\nlimit reached")
            break


    # SETUP FILE DEFAULT
    if setup == "":
        print(f"{DIM}{YELLOW}No setup file created{RESET}\n{YELLOW}●{RESET} Defaulting to create pyproject.toml\n")
        pyproj = create_pyprojecttoml(directory, description, keywords, author, author_mail, proj_name, licence, dependencies)
        setup = "pyproject.toml"
        time.sleep(0.5)

    # MAIN FILES
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


    # CREATING TEST FOLDER
    if test.lower() == 'y' or test.lower() == 'yes':
        os.makedirs(os.path.join(directory, 'test'))
        with open(os.path.join(directory, 'test', 'test.py'), 'w') as f:
            test = f"# {proj_name}/test/test.py\n"
            f.write(test)
            print(f"{tic}{proj_name}/test/test.py created successfully.{RESET}")
            time.sleep(0.5)
        test = True

    print(files_success)
    time.sleep(0.5)
    print(lst_file_display(proj_name, setup, test))
    time.sleep(0.5)
    print(ready_to_code)
    print(f"\n\t {BRIGHT_BLUE}cd{RESET} {directory}\n")
    print(footer)


# CHECK DIRECTORY
def check_directory(directory, proj_name):

    # Check if directory exists
    if not os.path.exists(directory):
        # options()
        print(f"{YELLOW}Directory doesn't exist.{RESET}")

        dir_loop = True
        while dir_loop:
            dir_crt = input(f"Do you like to create the directory? (y/n) [{CYAN}Y{RESET}] ")
            if dir_crt.lower() == 'y' or dir_crt.lower() == '':
                os.makedirs(directory)
                print(f"{tic}Directory created successfully.{RESET}\n")
                time.sleep(0.5)
                proj_name, description, keywords, author, author_mail, licence, dependencies = options(proj_name)
                create_files_and_folders(directory, description, keywords, author, author_mail, proj_name, licence, dependencies)
                dir_loop = False

            elif dir_crt.lower() == 'n':
                print(f"{RED}Creating project aborted.{RESET}")
                print(f"\n{footer}")
                sys.exit(1)

            else:
                print(invalid_input)

    else:
        try:
            # Check if directory is empty
            if not os.listdir(directory):
                proj_name, description, keywords, author, author_mail, licence, dependencies = options(proj_name)
                time.sleep(1.0)
                create_files_and_folders(directory, description, keywords, author, author_mail, proj_name, licence, dependencies)
            else:
                print(check_directory_err)
                list_dir(directory)

        except Exception as e:
            print(f"{BOLD}{RED}ERROR: {RESET}{e}")

def file_proj_name():
    directory = os.getcwd()
    proj_name = os.path.basename(directory)
    return proj_name

# MAIN (PIP CREATOR)
def pip_creator(directory, file):

    # if len(sys.argv) > 4 or len(sys.argv) < 3:
    #     print("Usage: pipcreator create <directory> ")
    #     sys.exit(1)


    if file:
        if os.path.exists(directory):
            print(f"{RED}File already exists.{RESET}")
            sys.exit(1)
        print(f"Creating {directory}...")
        with open(directory, 'w') as f:
            f.write(" ")
            print(f"{tic}{directory} created successfully.{RESET}")
            sys.exit(0)

    folder_name = ascii_lowercase + ascii_uppercase + digits + '_./'


    if "-" in directory:
        print(f"{YELLOW}The ' - ' will be replaced as '_' in the folder name{RESET}")
        directory = directory.replace("-", "_")

    if any(char not in folder_name for char in directory):
        print(f"{RED}Invalid directory name{RESET}")
        print(f"{YELLOW}Directory name must contain only the following characters:{RESET}")
        print("A-Z a-z 0-9 _ \n")
        print(footer)
        sys.exit(1)

    proj_name = file_proj_name()
    if directory == '.' or directory == './':
        directory = os.getcwd()

    elif directory.lower() == "readme.md":
        if os.path.exists(directory):
            print(f"{RED}File already exists.{RESET}")
            sys.exit(1)
        loop = True
        while loop:
            name = input(f"{BLUE}Project name {RESET}[{proj_name}]")
            if not name:
                name = proj_name
            desc = input(f"{BLUE}Description: {RESET}")
            if not desc:
                desc = " "
            loop = False
        print(f"Creating {directory}...")
        create_readme(".", desc, name)
        sys.exit(0)

    elif directory.lower() == "pyproject.toml":
        if os.path.exists(directory):
            print(f"{RED}File already exists.{RESET}")
            sys.exit(1)

        projname, description, keywords, author, author_mail, licence, dependencies = options(proj_name)
        print(f"Creating {directory}...")
        create_pyprojecttoml(".", description, keywords, author, author_mail, projname, licence, dependencies)
        sys.exit(0)

    elif directory.lower() == "setup.py":
        if os.path.exists(directory):
            print(f"{RED}File already exists.{RESET}")
            sys.exit(1)

        projname, description, keywords, author, author_mail, licence, dependencies = options(proj_name)
        print(f"Creating {directory}...")
        create_setuppy(".", description, keywords, author, author_mail, projname, licence, dependencies)
        sys.exit(0)

    elif directory.lower() == "requirements.txt":
        if os.path.exists(directory):
            print(f"{RED}File already exists.{RESET}")
            sys.exit(1)

        dependencies = input(f"{BLUE}Any dependencies for your project {RESET}")
        print(f"Creating {directory}...")
        create_requirements(".", dependencies)
        sys.exit(0)

    elif directory.lower() == ".gitignore":
        if os.path.exists(directory):
            print(f"{RED}File already exists.{RESET}")
            sys.exit(1)

        print(f"Creating {directory}...")
        create_gitignore(".")
        sys.exit(0)

    elif directory.lower() == "test.py":
        if os.path.exists("test"):
            print(f"{RED}Directory already exists.{RESET}")
            if os.path.exists("test/test.py"):
                print(f"{RED}File already exists.{RESET}")
                sys.exit(1)
            print(f"Creating {directory}...")
            os.makedirs(os.path.join(directory, 'test'))
            with open(os.path.join(directory, 'test', 'test.py'), 'w') as f:
                test = f"# {proj_name}/test/test.py\n"
                f.write(test)
                print(f"{tic}{proj_name}/test/test.py created successfully.{RESET}")
            
            sys.exit(0)
        
    proj_name = os.path.basename(directory)

    print(f'Creating project @ {BLUE}{os.getcwd()}{RESET}\n')

    check_directory(directory, proj_name)

