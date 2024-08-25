import click
import os
import sys

from textPlay import backend_exec
from textPlay.colors import *

from pipcreator.writer import pip_creator
from pipcreator.convert import run_setup_command_convert
from pipcreator.upload import run_setup_command_upload
from pipcreator.guide import guide_learn
from pipcreator.constants import title, footer
from pipcreator.install import install_package, uninstall_package, update_package, search_pypi_package, list_installed_packages, show_package_info

@click.group()
def cli():
    print(title)
    pass

@click.command()
@click.argument('directory')
@click.option('--file',is_flag=True, default=False, help='Create a new file')
@click.option('--folder',is_flag=True, default=False, help='Create a new folder')
def create(directory, file, folder):
    directory = str(directory)
    pip_creator(directory, file, folder)

@click.command()
def convert():
    run_setup_command_convert()

@click.command()
def upload():
    run_setup_command_upload()

@click.command()
def guide():
    guide_learn()

@click.command()
@click.argument('package')
def install(package):
    command = f"pip install {package}"
    if package == "requirements.txt" or package == "requirements" or package == "all-package":
        if not os.path.exists("requirements.txt"):
            print(f"{RED}requirements.txt does not exist{RESET}")
            print(f"\n{footer}")
            sys.exit(0)
        command = f"pip install -r requirements.txt"
    install_package(command)

@click.command()
@click.argument('package')
def uninstall(package):
    command = f"pip uninstall {package} -y"
    if package == "requirements.txt" or package == "requirements" or package == "all-package":
        if not os.path.exists("requirements.txt"):
            print(f"{RED}requirements.txt does not exist{RESET}")
            print(f"\n{footer}")
            sys.exit(0)
        command = f"pip uninstall -r requirements.txt -y"
    uninstall_package(command)

@click.command()
@click.argument('package')
def update(package):
    if package == "requirements.txt" or package == "requirements" or package == "all-package":
        if not os.path.exists("requirements.txt"):
            print(f"{RED}requirements.txt does not exist{RESET}")
            print(f"\n{footer}")
            sys.exit(0)
        command = f"pip install --upgrade -r requirements.txt"
    command = f"pip install {package} --upgrade"
    update_package(command, package)


@click.command()
@click.argument('package')
def search(package):
    search_results = search_pypi_package(package)
    for package in search_results:
        print(package)

@click.command()
def list():
    list_installed_packages()


@click.command()
@click.argument('package')
def show(package):
    show_package_info(package)



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