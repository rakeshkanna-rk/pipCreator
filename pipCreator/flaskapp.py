import os
import sys
from string import ascii_lowercase, ascii_uppercase, digits

from pipCreator.constants import *
from pipcreator.writer import virtual_env, create_pyprojecttoml, create_readme, create_requirements, create_gitignore, create_license
from textPlay.colors import *
from textPlay import list_dir

def file_proj_name():
    directory = os.getcwd()
    proj_name = os.path.basename(directory)
    return proj_name

def create_flask(directory):
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

    print(f'Creating project @ {BLUE}{os.getcwd()}{RESET}\n')
    check_directory(directory, proj_name)



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

    if dependencies:
        print("Creating virtual environment (venv) for safer installation...")
        venv_status = virtual_env("venv")
        
    pyproj = create_pyprojecttoml(directory, description, keywords, author, author_mail, proj_name, licence, dependencies)
    time.sleep(0.5)
    setup = "pyproject.toml"



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
    flask_app = create_app(directory, proj_name)


    # CREATING TEST FOLDER
    if test.lower() == 'y' or test.lower() == 'yes':
        os.makedirs(os.path.join(directory, 'test'))
        with open(os.path.join(directory, 'test', 'test_basic.py'), 'w') as f:
            f.write(test_basic)
            print(f"{tic}{proj_name}/test/test_basic.py created successfully.{RESET}")
            time.sleep(0.5)

        with open(os.path.join(directory, 'test', 'conftest.py'), 'w') as f:
            f.write(tests_conftest)
            print(f"{tic}{proj_name}/test/conftest.py created successfully.{RESET}")
            time.sleep(0.5)
        test = True

    if venv_status:
        print(f"\nHow to Using/Activation virtual environment\n   use: {MAGENTA}pipc guide --see on-venv{RESET}")
        time.sleep(1.0)

    print(files_success)
    time.sleep(0.5)
    print(lst_file_display(proj_name, test))
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
                dependencies = flask_requirements + dependencies
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
                dependencies = "Flask==2.3.2 Flask-SQLAlchemy==3.0.3 Flask-Migrate==4.0.4 Flask-WTF==1.0.1  " + dependencies
                time.sleep(1.0)
                create_files_and_folders(directory, description, keywords, author, author_mail, proj_name, licence, dependencies)
            else:
                print(check_directory_err)
                list_dir(directory)

        except Exception as e:
            print(f"{BOLD}{RED}ERROR: {RESET}{e}")


def create_app(directory, proj_name):

    os.makedirs(os.path.join(directory, 'app'))

    with open(os.path.join(directory, 'app', '__init__.py'), 'w') as f:
        f.write(app_init)
        print(f"{tic}{proj_name}/app/__init__.py created successfully.{RESET}")
        time.sleep(0.5)
    
    with open(os.path.join(directory, 'app', 'routes.py'), 'w') as f:
        f.write(app_routes)
        print(f"{tic}{proj_name}/app/routes.py created successfully.{RESET}")
        time.sleep(0.5)


    with open(os.path.join(directory, 'app', 'forms.py'), 'w') as f:
        f.write(app_forms) 
        print(f"{tic}{proj_name}/app/forms.py created successfully.{RESET}")
        time.sleep(0.5)

    with open(os.path.join(directory, 'app', 'models.py'), 'w') as f:
        f.write(app_models)
        print(f"{tic}{proj_name}/app/models.py created successfully.{RESET}")
        time.sleep(0.5)

    # TEMPLATE
    os.makedirs(os.path.join(directory, 'app', 'templates'))
    with open(os.path.join(directory, 'app', 'templates', 'layout.html'), 'w') as f:
        f.write(app_template_layout)
        print(f"{tic}{proj_name}/app/templates/layout.html created successfully.{RESET}")
        time.sleep(0.5)

    with open(os.path.join(directory, 'app', 'templates', 'home.html'), 'w') as f:
        f.write(app_template_home)
        print(f"{tic}{proj_name}/app/templates/home.html created successfully.{RESET}")
        time.sleep(0.5)

    # STATIC
    os.makedirs(os.path.join(directory, 'app', 'static'))
    with open(os.path.join(directory, 'app', 'static', 'css', 'style.css'), 'w') as f:
        f.write(app_static_css)
        print(f"{tic}{proj_name}/app/static/css/style.css created successfully.{RESET}")
        time.sleep(0.5)

    os.makedirs(os.path.join(directory, 'app', 'static', 'js'))
    with open(os.path.join(directory, 'app', 'static', 'js', 'script.js'), 'w') as f:
        f.write(app_static_js)
        print(f"{tic}{proj_name}/app/static/js/script.js created successfully.{RESET}")
        time.sleep(0.5)

    os.makedirs(os.path.join(directory, 'app', 'static', 'images'))
    print(f"{tic}{proj_name}/app/static/images/ created successfully.{RESET}")
    time.sleep(0.5)

    # MIGRATIONS
    os.makedirs(os.path.join(directory, 'migrations'))
    print(f"{tic}{proj_name}/migrations/ created successfully.{RESET}")
    time.sleep(0.5)

    # INSTANCE
    os.makedirs(os.path.join(directory, 'instance'))
    with open(os.path.join(directory, 'instance', 'config.py'), 'w') as f:
        f.write(instance_config)
        print(f"{tic}{proj_name}/instance/config.py created successfully.{RESET}")
        time.sleep(0.5)

    with open(os.path.join(directory, 'config.py'), 'w') as f:
        f.write(config)
        print(f"{tic}{proj_name}/config.py created successfully.{RESET}")
        time.sleep(0.5)

    with open(os.path.join(directory, 'run.py'), 'w') as f:
        f.write(run)
        print(f"{tic}{proj_name}/run.py created successfully.{RESET}")
        time.sleep(0.5)
    