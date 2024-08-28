# FLASK APP TEMPLATE =========================================================

import os
import time
from pipcreator.constants import tic
from textPlay.colors import *

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

# Basic Flask App =========================================================
basic_flask_app = '''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)

'''


# CREATE TEMPLATE =========================================================

def template(directory, proj_name, path = os.path.join('app', 'templates')):
    # TEMPLATE
    os.makedirs(os.path.join(directory, path))
    with open(os.path.join(directory, path, 'layout.html'), 'w') as f:
        f.write(app_template_layout)
        print(f"{tic}{proj_name}/{path}/layout.html created successfully.{RESET}")
        time.sleep(0.5)

    with open(os.path.join(directory, path, 'home.html'), 'w') as f:
        f.write(app_template_home)
        print(f"{tic}{proj_name}/{path}/home.html created successfully.{RESET}")
        time.sleep(0.5)

# CREATE APP ==============================================================
def app(directory, proj_name,path = "app"):

    os.makedirs(os.path.join(directory, path), exist_ok=True)

    with open(os.path.join(directory, path, '__init__.py'), 'w') as f:
        f.write(app_init)
        print(f"{tic}{proj_name}/app/__init__.py created successfully.{RESET}")
        time.sleep(0.5)
    
    with open(os.path.join(directory, path, 'routes.py'), 'w') as f:
        f.write(app_routes)
        print(f"{tic}{proj_name}/app/routes.py created successfully.{RESET}")
        time.sleep(0.5)

    with open(os.path.join(directory, path, 'forms.py'), 'w') as f:
        f.write(app_forms) 
        print(f"{tic}{proj_name}/app/forms.py created successfully.{RESET}")
        time.sleep(0.5)

    with open(os.path.join(directory, path, 'models.py'), 'w') as f:
        f.write(app_models)
        print(f"{tic}{proj_name}/{path}/models.py created successfully.{RESET}")
        time.sleep(0.5)


# CREATE APP STATIC ======================================================
def app_static(directory, proj_name, path= os.path.join('app', 'static')):
    # STATIC
    os.makedirs(os.path.join(directory, path))

    os.makedirs(os.path.join(directory, path, 'css'))
    with open(os.path.join(directory, path, 'css', 'style.css'), 'w') as f:
        f.write(app_static_css)
        print(f"{tic}{proj_name}/{path}/css/style.css created successfully.{RESET}")
        time.sleep(0.5)

    os.makedirs(os.path.join(directory, path, 'js'))
    with open(os.path.join(directory, 'app', 'static', 'js', 'script.js'), 'w') as f:
        f.write(app_static_js)
        print(f"{tic}{proj_name}/{path}/js/script.js created successfully.{RESET}")
        time.sleep(0.5)

    os.makedirs(os.path.join(directory, 'app', 'static', 'images'))
    print(f"{tic}{proj_name}/{path}/images/ created successfully.{RESET}")
    time.sleep(0.5)


# FLASK DIRECTORY =========================================================
def flask_directory(directory, proj_name):
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


# BASIC APP ============================================================== 

def basic_app(directory, proj_name):
    with open(os.path.join(directory, 'app.py'), 'w') as f:
        f.write(basic_flask_app)
        print(f"{tic}{proj_name}/app.py created successfully.{RESET}")
        time.sleep(0.5)


# REACT FRAMEWORK ========================================================
from textPlay import backend_exec
from pipcreator.constants import error_msg

def app_react(directory, proj_name):

    try:
        backend_exec("npx create-react-app@latest client")
        print(f"{tic}{proj_name}/client created successfully.{RESET}")
    except Exception as e:
        print(error_msg," ",e)

def app_nextjs(directory, proj_name):

    try:
        backend_exec("npx create-next-app@latest client")
        print(f"{tic}{proj_name}/client created successfully.{RESET}")
    except Exception as e:
        print(error_msg," ",e)

def app_vite(directory, proj_name):

    try:
        backend_exec("npx create-vite@latest client")
        print(f"{tic}{proj_name}/client/vite created successfully.{RESET}")
    except Exception as e:
        print(error_msg," ",e)

def other_framework(directory, proj_name, script):

    try:
        if script:
            backend_exec(script)
            print(f"{tic}{proj_name}/client created successfully.{RESET}")
        else:
            print(error_msg," No script provided")

    except Exception as e:
        print(error_msg," ",e)