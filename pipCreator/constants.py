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

from pipcreator.install import check_requirements, update_setup, update_toml

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
            update_toml(setup_file='pyproject.toml', new_dependencies=content)

    if os.path.exists("setup.py"):
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



# FLASK APP TEMPLATE =========================================================


# FLASK APP TEMPLATE
def flask_structure(project_name, test=False):
    if test:
        flask_app = f'''
{project_name}/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── layout.html
│       └── home.html
│
├── config.py
├── README.md
├── run.py
├── requirements.txt
├── pyproject.toml
├── venv/
├── instance/
│   └── config.py
├── migrations/
├── tests/
│   ├── test_basic.py
│   └── conftest.py
└── .env or .flaskenv
'''
    else:
        flask_app = f'''
{project_name}/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── layout.html
│       └── home.html
│
├── config.py
├── README.md
├── run.py
├── requirements.txt
├── pyproject.toml
├── venv/
├── instance/
│   └── config.py
├── migrations/
└── .env or .flaskenv
'''
    return flask_app



# app/__init__.py
app_init = '''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load the configuration from config.py
    app.config.from_object('config.Config')
    
    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    
    # Import and register Blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
'''

# app/routes.py
app_routes = '''
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

'''

# app/models.py
app_models = '''
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

'''

# app/forms.py
app_forms = '''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

'''

# app/static/css/style.css
app_static_css = '''
body {
    font-family: Arial, sans-serif;
    background-color: #f8f9fa;
}

h1 {
    color: #343a40;
}
'''

# app/static/js/script.js
app_static_js = '''
console.log("Hello, World!");
'''

# app/templates/layout.html
app_template_layout = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <title>Flask App</title>
</head>
<body>
    <header>
        <h1>Welcome to Flask App</h1>
    </header>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
'''

# app/templates/home.html
app_template_home = '''
{% extends 'layout.html' %}

{% block content %}
    <h1>Home</h1>
    <p>This is the home page.</p>
{% endblock %}
'''

# config.py
config = '''
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

'''

# run.py
run = '''
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

'''

# requirements.txt
flask_requirements = "Flask==2.3.2 Flask-SQLAlchemy==3.0.3 Flask-Migrate==4.0.4 Flask-WTF==1.0.1 pytest "

# instance/config.py
instance_config = '''
# This is used for instance-specific configuration
# Do not add this file to version control
SECRET_KEY = 'instance-specific-secret-key'
'''

# tests/test_basic.py
test_basic = '''
import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home Page' in response.data

'''

# tests/conftest.py
tests_conftest = '''
# This file can be used to define common test configurations
import pytest
from app import create_app, db

@pytest.fixture(scope='module')
def new_app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def client(new_app):
    return new_app.test_client()

@pytest.fixture(scope='module')
def init_database(new_app):
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
'''

# .flaskenv
flask_env = '''
FLASK_APP=app.py
FLASK_ENV=development
FLASK_RUN_PORT=5000
FLASK_RUN_HOST=0.0.0.0
'''