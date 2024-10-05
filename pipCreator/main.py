import click
import os
import sys

from textPlay import backend_exec
from textPlay.colors import *

from pipcreator.writer import pip_creator
from pipcreator.convert import run_setup_command_convert
from pipcreator.upload import run_setup_command_upload
from pipcreator.guide import *
from pipcreator.constants import title, footer, tic, update_dependencies
from pipcreator.package import install_package, uninstall_package, update_package, search_pypi_package, list_installed_packages, show_package_info

from pipcreator.plugin import git_fetch


@click.group()
def cli():
    print(title)
    pass

@click.command(help='Create a new python project')
@click.argument('directory')
@click.option('--file',is_flag=True, default=False, help='Create a new file')
@click.option('--folder',is_flag=True, default=False, help='Create a new folder')
@click.option('--pluign',is_flag=True, default=False, help='Create a new plugin app')
def create(directory, file, folder, pluign):
    if pluign:
        directory = directory.replace("-", "_")
        cmd = git_fetch("commands", directory)
        backend_exec(cmd)
    else:
        directory = str(directory)
        pip_creator(directory, file, folder)

@click.command()
def convert(help='Convert setup.py or pyproject.toml to distribution file'):
    run_setup_command_convert()

@click.command(help='Upload distribution file to PyPI')
def upload():
    run_setup_command_upload()

@click.command(help='Show guide with on topics `all` or `on-<topic>`')
@click.option('--see', help='See the guide  on topics `all` or `on-<topic>`')
def guide(see):
    if see=="all":
        guide_learn()

    web_guide(see)
    

@click.command(help='Install package with clear visuals')
@click.argument('package', required=False)
@click.option('--no-req',is_flag=True, default=False)
@click.option('--plugin', is_flag=True, default=False) # TODO : Create plugin option || Delete flask file in flaskapp.py ad flask_constants.py
def install(package, no_req, plugin):
    # TODO : Add all plugin function


    if plugin:
        plugin_name = package
        if plugin_name.lower() == "pipc.all-plugins":
            pkg = git_fetch("all-plugins")
            print("PIPC PLUGINS")
            for i in pkg:
                print(f" - {BLUE}{i}{RESET}")
            package = " ".join(pkg)
            
        
        else:
            try:
                pkg = git_fetch("plugins", plugin_name)
                if plugin_name not in pkg:
                    print(f"{RED}Plugin {package} not found{RESET}")
                    
                    sys.exit(0)

                else:
                    print("PIPC PLUGIN")
                    print(f" - {BLUE}{plugin_name}{RESET}")
                    package = " ".join(pkg)

            except Exception as e:
                print(f"{RED}Plugin {package} not found{RESET}")
                
                sys.exit(0)

    else:
        raise NotImplementedError
    


    command = f"pip install {package}"
    if package == "requirements.txt" or package == "requirements" or package == "all" and not no_req:
        if not os.path.exists("requirements.txt"):
            print(f"{RED}requirements.txt does not exist{RESET}")
            
            sys.exit(0)
        command = f"pip install -r requirements.txt"
    installed, already_installed = install_package(command)

    update_dependencies(installed, already_installed)

    if plugin:
        print(f"{tic}All plugins installed successfully.{RESET}")
        
    else:
        print(f"{tic}Package installed successfully.{RESET}")
        



@click.command(help='Uninstall package with clear visuals')
@click.argument('package')
@click.option('--no-req',is_flag=True, default=False)
def uninstall(package, no_req):
    command = f"pip uninstall {package} -y"
    if package == "requirements.txt" or package == "requirements" or package == "all-packages" and not no_req:
        if not os.path.exists("requirements.txt"):
            print(f"{RED}requirements.txt does not exist{RESET}")
            
            sys.exit(0)
        command = f"pip uninstall -r requirements.txt -y"
    uninstall_package(command)
    

@click.command(help='Update package with clear visuals')
@click.argument('package')
@click.option('--no-req',is_flag=True, default=False)
def update(package, no_req):
    if package == "requirements.txt" or package == "requirements" or package == "all-packages" and not no_req:
        if not os.path.exists("requirements.txt"):
            print(f"{RED}requirements.txt does not exist{RESET}")
            
            sys.exit(0)
        command = f"pip install --upgrade -r requirements.txt"
    command = f"pip install {package} --upgrade"
    update_package(command, package)
    


@click.command(help='Search package with clear visuals')
@click.argument('package')
def search(package):
    search_results = search_pypi_package(package)
    for package in search_results:
        print(package)
    

@click.command(help='List all installed packages')
def list():
    list_installed_packages()
    


@click.command(help='Show package info with clear visuals')
@click.argument('package')
def show(package):
    show_package_info(package)
    

@click.command(help='Create all necessary files for flask app')
@click.argument('directory')
def create_flask_app(directory):
    try:
        from pipc_flask_app.flaskapp import create_flask
        create_flask(directory)
    except Exception as e:
        print(f"{RED}Plugin not found. {RESET}\nUse {MAGENTA}pipc install pipc.flask_app --plugin{RESET} to install the plugin.")
        print("Error", e)

cli.add_command(create)
cli.add_command(convert)
cli.add_command(upload)
cli.add_command(guide)
cli.add_command(install)
cli.add_command(uninstall)
cli.add_command(update)
cli.add_command(search)
cli.add_command(list)
cli.add_command(show)
cli.add_command(create_flask_app)

print(f"\n{footer}")