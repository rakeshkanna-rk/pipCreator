import click
import os
import sys

from textPlay import backend_exec
from textPlay.colors import *

from pipcreator.writer import pip_creator
from pipcreator.convert import run_setup_command_convert
from pipcreator.upload import run_setup_command_upload
from pipcreator.guide import *
from pipcreator.constants import title, footer, update_dependencies
from pipcreator.package import install_package, uninstall_package, update_package, search_pypi_package, list_installed_packages, show_package_info
from pipcreator.git import git_clone_repository, git_commit_and_push

from pipCreator.plugin import git_fetch

from pipc_flask_app.flaskapp import create_flask



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
@click.option('--see', help='See the guide with on topics `all` or `on-<topic>`')
def guide(see):
    if see=="all":
        guide_learn()

    web_guide(see)
    

@click.command()
@click.argument('package', required=False)
@click.option('--no-req',is_flag=True, default=False)
@click.option('--plugin', default="pipc.all-plugins") # TODO : Create plugin option || Delete flask file in flaskapp.py ad flask_constants.py
def install(package, no_req, plugin):
    # TODO : Add all plugin function
    plugin_name = plugin[4:].replace("-", "_")
    if plugin.lower() == "pipc.all-plugins":
        pkg = git_fetch("all-plugins")
        print("PIPC PLUGINS")
        for i in pkg:
            print(f" - {BLUE}{i}{RESET}")
        package = " ".join(pkg)
    
    else:
        try:
            pkg = git_fetch("packages", plugin_name)
            if plugin_name not in pkg:
                print(f"{RED}Plugin {package} not found{RESET}")
                print(f"\n{footer}")
                sys.exit(0)

            else:
                print("PIPC PLUGIN")
                print(f" - {BLUE}{plugin_name}{RESET}")
                package = pkg

        except Exception as e:
            print(f"{RED}Plugin {package} not found{RESET}")
            print(f"\n{footer}")
            sys.exit(0)


    command = f"pip install {package}"
    if package == "requirements.txt" or package == "requirements" or package == "all" and not no_req:
        if not os.path.exists("requirements.txt"):
            print(f"{RED}requirements.txt does not exist{RESET}")
            print(f"\n{footer}")
            sys.exit(0)
        command = f"pip install -r requirements.txt"
    installed, already_installed = install_package(command)

    update_dependencies(installed, already_installed)

    print(f"\n{footer}")



@click.command()
@click.argument('package')
@click.option('--no-req',is_flag=True, default=False)
def uninstall(package, no_req):
    command = f"pip uninstall {package} -y"
    if package == "requirements.txt" or package == "requirements" or package == "all-packages" and not no_req:
        if not os.path.exists("requirements.txt"):
            print(f"{RED}requirements.txt does not exist{RESET}")
            print(f"\n{footer}")
            sys.exit(0)
        command = f"pip uninstall -r requirements.txt -y"
    uninstall_package(command)
    print(f"\n{footer}")

@click.command()
@click.argument('package')
@click.option('--no-req',is_flag=True, default=False)
def update(package, no_req):
    if package == "requirements.txt" or package == "requirements" or package == "all-packages" and not no_req:
        if not os.path.exists("requirements.txt"):
            print(f"{RED}requirements.txt does not exist{RESET}")
            print(f"\n{footer}")
            sys.exit(0)
        command = f"pip install --upgrade -r requirements.txt"
    command = f"pip install {package} --upgrade"
    update_package(command, package)
    print(f"\n{footer}")


@click.command()
@click.argument('package')
def search(package):
    search_results = search_pypi_package(package)
    for package in search_results:
        print(package)
    print(f"\n{footer}")

@click.command()
def list():
    list_installed_packages()
    print(f"\n{footer}")


@click.command()
@click.argument('package')
def show(package):
    show_package_info(package)
    print(f"\n{footer}")


@click.command()
@click.option('--repo-url', help='Repository URL to clone')
@click.option('--path', default=None, help='Path to Save Repository')
def clone(repo_url, path):
    if repo_url:
        if not path:
            path = os.getcwd()
            git_clone_repository(repo_url, path)
    else:
        print("Please specify a repository URL with --repo-url")
    print(f"\n{footer}")


@click.command()
@click.option("--msg", "-m", default=None, help="Commit message")
def commit(msg):
    git_commit_and_push(msg)
    print(f"\n{footer}")

@click.command()
@click.argument('directory')
def create_flask_app(directory):
    create_flask(directory)


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
cli.add_command(clone)
cli.add_command(commit)
cli.add_command(create_flask_app)