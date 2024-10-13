# CLI
from .main import cli

# WRITER
from .writer import pip_creator

# OTHER FUNCTIONS
from .writer import create_gitignore, create_license
from .writer import create_pyprojecttoml, create_readme
from .writer import create_requirements, create_setuppy

# CONVERT
from .convert import run_setup_command_convert

# UPLOAD
from .upload import run_setup_command_upload

# GUIDE
from .guide import guide_learn, web_guide

# PACKAGE MANGEMENT
from .package import install_package, uninstall_package, update_package, search_pypi_package, list_installed_packages, show_package_info, update_toml, update_setup, update_dependencies, check_package

# PLUGIN
from .plugin import git_fetch

__create__ = ["pip_creator"]

__create_files__ = ["create_gitignore", "create_license", 
                    "create_pyprojecttoml", "create_readme", 
                    "create_requirements", "create_setuppy"]

__build__ = ["run_setup_command"]

__upload__ = ["run_setup_command_upload"]

__guide__ = ["guide_learn"]

__package__ = ["install_package", "uninstall_package", "update_package", "search_pypi_package", "list_installed_packages", "show_package_info", "update_toml", "update_setup", "update_dependencies"]

__all__ = __create__ + __create_files__  + __build__ + __upload__ + __guide__ + __package__ 
