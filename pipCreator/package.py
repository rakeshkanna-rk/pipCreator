import subprocess
import re
import itertools
import sys
import os
import time
import threading
import subprocess
import pkg_resources
import requests
import textwrap
from bs4 import BeautifulSoup

from textPlay.colors import *
from pipcreator.constants import tic, footer, error_msg, warn


# SPINNER ANIMATION =========================================

install_animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

def spinner_animation(stop_event):
    spinner = itertools.cycle(install_animation)
    while not stop_event.is_set():
        sys.stdout.write(next(spinner))  # Write the next spinner character
        sys.stdout.flush()               # Force the character to display
        time.sleep(0.1)                  # Wait a bit before the next character
        sys.stdout.write('\b')           # Backspace to overwrite the character

    # Clear the spinner when stopping
    sys.stdout.write(' ')  # Write a space to clear the spinner
    sys.stdout.write('\b') # Move back again to overwrite the space with the next output




# INSTALL PACKAGES =========================================

def install_package(command):
    try:
        # Create a threading event to control the spinner
        stop_spinner = threading.Event()
        spinner_thread = threading.Thread(target=spinner_animation, args=(stop_spinner,))

        # Start the spinner in a separate thread
        spinner_thread.start()

        # Capture both stdout and stderr
        result = subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Stop the spinner after the command completes
        stop_spinner.set()
        spinner_thread.join()  # Ensure spinner thread finishes

        installed_packages = []
        already_installed_packages = []
        warnings = []
        errors = []

        # Check the return code to determine success
        if result.returncode == 0:
            print(f"Success: Package installed successfully.")
            
            # Track installed packages and already installed packages
            installed_packages, already_installed_packages = track_installed_packages(result.stdout)
        else:
            print("\nError: An error occurred during the installation.")
            errors.append(result.stderr)
        
        # Capture warnings
        if result.stderr:
            warnings = track_warnings(result.stderr)

        # Display the installed packages
        if installed_packages:
            print("\nInstalled packages:")
            for pkg in installed_packages:
                print(f" - {pkg}")

        # Display already installed packages
        if already_installed_packages:
            print("\nAlready installed packages:")
            for pkg in already_installed_packages:
                print(f" - {pkg}")

        # Summary of the process
        installed = f"{GREEN}({len(installed_packages)}) installed{RESET}"
        already_installed = f"{CYAN}({len(already_installed_packages)}) pre-installed{RESET}"
        warning_count = f"{YELLOW}({len(warnings)}) warning(s){RESET}"
        error_count = f"{RED}({len(errors)}) error(s){RESET}"
        print(f"\nSummary: \n   {installed}, {already_installed}, {warning_count}, {error_count}")

        # Display warnings and errors
        if warnings:
            print(f"\n{warn}")
            for warning in warnings:
                print(f" - {warning}")

        if errors:
            print(f"\n{error_msg}")
            for error in errors:
                print(f" - {error}")

    except subprocess.CalledProcessError as e:
        print(f"\nError: Command '{command}' failed with return code {e.returncode}.")
        print(e.output)

    except Exception as e:
        print(f"\nError: {e}")

    return installed_packages, already_installed_packages

def track_installed_packages(output):
    """
    Parse the output of the installation command to extract the names of installed packages
    and those that were already installed.
    """
    installed_packages = []
    already_installed_packages = []
    install_pattern = re.compile(r"Successfully installed ([^\s]+(?: [^\s]+)*)")
    already_installed_pattern = re.compile(r"Requirement already satisfied: ([^\s]+)")

    for line in output.splitlines():
        install_match = install_pattern.search(line)
        already_installed_match = already_installed_pattern.search(line)
        if install_match:
            package = install_match.group(1).split()
            installed_packages.extend(package)
        elif already_installed_match:
            package = already_installed_match.group(1)
            already_installed_packages.append(package)
    
    return installed_packages, already_installed_packages

def track_warnings(stderr):
    """
    Parse the stderr output to extract warning messages.
    """
    warnings = []
    warning_keywords = ["warning", "deprecated"]

    for line in stderr.splitlines():
        if any(keyword in line.lower() for keyword in warning_keywords):
            warnings.append(line.strip())

    return warnings



# UNINSTALL PACKAGE =========================================

# Define the animation sequence
def uninstall_package(command):
    try:
        # Create a threading event to control the spinner
        stop_spinner = threading.Event()
        spinner_thread = threading.Thread(target=spinner_animation, args=(stop_spinner,))

        # Start the spinner in a separate thread
        spinner_thread.start()

        # Capture both stdout and stderr
        result = subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Stop the spinner after the command completes
        stop_spinner.set()
        spinner_thread.join()  # Ensure spinner thread finishes

        uninstalled_packages = []
        not_installed_packages = []
        warnings = []
        errors = []

        # Check the return code to determine success
        if result.returncode == 0:
            print("\nSuccess: Package uninstalled successfully.")
            
            # Track uninstalled packages and packages not found
            uninstalled_packages, not_installed_packages = track_uninstalled_packages(result.stdout)
        else:
            print("\nError: An error occurred during the uninstallation.")
            errors.append(result.stderr)
        
        # Capture warnings
        if result.stderr:
            warnings = track_warnings(result.stderr)

        # Display the uninstalled packages
        if uninstalled_packages:
            print("\nUninstalled packages:")
            for pkg in uninstalled_packages:
                print(f" - {pkg}")

        # Display packages not found or already uninstalled
        if not_installed_packages:
            print("\nPackages not installed or already removed:")
            for pkg in not_installed_packages:
                print(f" - {pkg}")

        # Summary of the process
        uninstalled = f"{GREEN}({len(uninstalled_packages)}) uninstalled{RESET}"
        not_installed = f"{CYAN}({len(not_installed_packages)}) not installed{RESET}"
        warning_count = f"{YELLOW}({len(warnings)}) warning(s){RESET}"
        error_count = f"{RED}({len(errors)}) error(s){RESET}"
        print(f"\nSummary: \n   {uninstalled}, {not_installed}, {warning_count}, {error_count}")

        # Display warnings and errors
        if warnings:
            print(f"\n{warn}")
            for warning in warnings:
                print(f" - {warning}")

        if errors:
            print(f"\n{error_msg}")
            for error in errors:
                print(f" - {error}")

    except subprocess.CalledProcessError as e:
        # Ensure spinner is stopped in case of an exception
        stop_spinner.set()
        spinner_thread.join()
        print(f"\nError: Command '{command}' failed with return code {e.returncode}.")
        print(e.output)

    except Exception as e:
        print(f"\nError: {e}")

    finally:
        print(f"\n{footer}")

def track_uninstalled_packages(output):
    """
    Parse the output of the uninstallation command to extract the names of uninstalled packages
    and those that were not installed.
    """
    uninstalled_packages = []
    not_installed_packages = []
    uninstall_pattern = re.compile(r"Successfully uninstalled ([^\s]+)")
    not_installed_pattern = re.compile(r"WARNING: Skipping ([^\s]+) as it is not installed")

    for line in output.splitlines():
        uninstall_match = uninstall_pattern.search(line)
        not_installed_match = not_installed_pattern.search(line)
        if uninstall_match:
            package = uninstall_match.group(1)
            uninstalled_packages.append(package)
        elif not_installed_match:
            package = not_installed_match.group(1)
            not_installed_packages.append(package)
    
    return uninstalled_packages, not_installed_packages

def track_warnings(stderr):
    """
    Parse the stderr output to extract warning messages.
    """
    warnings = []
    warning_keywords = ["warning", "deprecated"]

    for line in stderr.splitlines():
        if any(keyword in line.lower() for keyword in warning_keywords):
            warnings.append(line.strip())

    return warnings



# UPDATE PACKAGE =========================================

def update_package(command, package_name):
    try:
        # Check the current version before updating
        current_version = get_package_version(package_name)
        print(f"Current version of {package_name}: {current_version}")

        # Create an event to stop the spinner
        stop_event = threading.Event()

        # Start the spinner animation in a separate thread
        spinner_thread = threading.Thread(target=spinner_animation, args=(stop_event,))
        spinner_thread.start()

        # Update the package
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Stop the spinner
        stop_event.set()
        spinner_thread.join()

        updated_version = get_package_version(package_name)

        # Lists to track updated and up-to-date packages
        updated_packages = []
        up_to_date_packages = []
        warnings = []
        errors = []

        # Determine if the package was updated
        if result.returncode == 0:
            if updated_version != current_version:
                updated_packages.append(f"{package_name}-{updated_version}")
                print(f"\nSuccess: Package '{package_name}' updated successfully.")
            else:
                up_to_date_packages.append(package_name)
                print(f"\nNote: Package '{package_name}' is already at the latest version.")
        else:
            errors.append(result.stderr)
            print(f"\nError: An error occurred during the update.")
            print(f"Error details:\n{result.stderr}")

        # Capture any warnings
        if result.stderr:
            warnings.extend(track_warnings(result.stderr))

        if updated_packages:
            print("\nUpdated packages:")
            for pkg in updated_packages:
                print(f" - {pkg}")

        if up_to_date_packages:
            print("\nPackages already at the latest version:")
            for pkg in up_to_date_packages:
                print(f" - {pkg}")

        # Summary of the process
        updated = f"{GREEN}({len(updated_packages)}) updated{RESET}"
        up_to_date = f"{CYAN}({len(up_to_date_packages)}) up to date{RESET}"
        warning_count = f"{YELLOW}({len(warnings)}) warning(s){RESET}"
        error_count = f"{RED}({len(errors)}) error(s){RESET}"
        print(f"\nSummary: \n   {updated}, {up_to_date}, {warning_count}, {error_count}")

        if warnings:
            print(f"\n{warn}")
            for warning in warnings:
                print(f" - {warning}")

        if errors:
            print(f"\n{error_msg}")
            for error in errors:
                print(f" - {error}")

    except Exception as e:
        print(f"An error occurred: {e}")

def get_package_version(package_name):
    result = subprocess.run(f"pip show {package_name}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    version_line = next((line for line in result.stdout.splitlines() if line.startswith("Version:")), None)
    if version_line:
        return version_line.split(":", 1)[1].strip()
    return None

def track_warnings(stderr):
    """
    Parse the stderr output to extract warning messages.
    """
    warnings = []
    warning_keywords = ["warning", "deprecated"]

    for line in stderr.splitlines():
        if any(keyword in line.lower() for keyword in warning_keywords):
            warnings.append(line.strip())

    return warnings

# SEARCH PACKAGE =========================================


# Define the color codes as needed
colors = {
    "BOLD": LIGHT_WHITE,
    "RESET": "\033[0m",
    "BLUE": "\033[34m",
}

def search_pypi_package(search_term):
    url = f"https://pypi.org/search/?q={search_term}"
    headers = {
        "User-Agent": "pip-search-script",
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Parse the response to extract package names, versions, and descriptions
        packages = []
        soup = BeautifulSoup(response.text, 'html.parser')
        
        results = soup.find_all("a", class_="package-snippet")
        for result in results:
            name = result.find("span", class_="package-snippet__name").text
            version = result.find("span", class_="package-snippet__version").text
            description = result.find("p", class_="package-snippet__description").text.strip()
            
            # Format the output with equal spacing and color codes
            package_info = f"{colors['BOLD']}{name} ({version}){colors['RESET']}"
            formatted_info = f"{package_info:<35} : {colors['BLUE']}{description}{colors['RESET']}"
            
            packages.append(formatted_info)
        
        return packages
    else:
        raise Exception(f"Failed to fetch data from PyPI: {response.status_code}")



# LIST PACKAGES =========================================


def list_installed_packages():
    # Get the list of installed packages
    installed_packages = sorted([(d.project_name, d.version) for d in pkg_resources.working_set])


    # Display each package with name, version, and colors
    for package, version in installed_packages:
        package_info = f"{package} ({BLUE}{version}{RESET})"
        print(package_info)

    # Display the total number of installed packages
    print(f"\n  {BOLD}Total Installed Packages: {GREEN}{len(installed_packages)}{RESET}")



# SHOW PACKAGE INFO =========================================


def show_package_info(package_name):
    try:
        # Use subprocess to run 'pip show <package>'
        result = subprocess.run(["pip", "show", package_name], capture_output=True, text=True)
        if result.returncode == 0:
            # Parse the output and add colors
            lines = result.stdout.splitlines()
            for line in lines:
                if line.startswith("Name:"):
                    print(f"{BOLD}{line}{RESET}")
                elif line.startswith("Version:"):
                    print(f"{BLUE}{line}{RESET}")
                elif line.startswith("Summary:"):
                    print(f"{GREEN}{line}{RESET}")
                elif line.startswith("Home-page:"):
                    print(f"{YELLOW}{line}{RESET}")
                else:
                    print(line)
        else:
            print(f"{RED}Package '{package_name}' not found.{RESET}")
    except Exception as e:
        print(f"{RED}An error occurred: {e}{RESET}")





# UPDATE PACKAGE IN REQUIREMENTS and SETUP =========================================

# UPDATE SETUP.PY ===============================================================

def get_current_dependencies(setup_file='setup.py'):
    with open(setup_file, 'r') as file:
        content = file.read()
    match = re.search(r"install_requires\s*=\s*\[(.*?)\]", content, re.DOTALL)
    if match:
        # Extract and clean the dependency list
        dependencies = match.group(1).split(',')
        dependencies = [dep.strip().strip("'\"") for dep in dependencies]
        return dependencies
    else:
        raise ValueError("install_requires list not found in setup.py")

def set_dependencies(new_dependencies, setup_file='setup.py'):
    # Get the current dependencies from the file
    current_dependencies = get_current_dependencies(setup_file)

    if '' in new_dependencies:
        new_dependencies.remove('')

    if '' in current_dependencies:
        current_dependencies.remove('')

    # Merge the current dependencies with new ones
    combined_dependencies = list(set(current_dependencies + new_dependencies))

    # Format the combined dependencies list
    formatted_deps = ', '.join([f"'{dep.strip()}'" for dep in combined_dependencies])

    # Replace the install_requires list with the updated dependencies
    with open(setup_file, 'r') as file:
        content = file.read()

    new_content = re.sub(r"install_requires\s*=\s*\[.*?\]", f"install_requires=[{formatted_deps}]", content, flags=re.DOTALL)

    with open(setup_file, 'w') as file:
        file.write(new_content)

def update_setup(setup_file='setup.py', new_dependencies=[]):
    if not os.path.exists(setup_file):
        raise FileNotFoundError(f"File not found: {setup_file}")
    else:
        try:
            print(f"Updating {setup_file}...")

            # Updating dependencies in setup.py
            set_dependencies(new_dependencies, setup_file)
            
            # Displaying updated dependencies
            updated_dependencies = get_current_dependencies(setup_file)
            print(f"{GREEN}Updated dependencies:{RESET}")
            for dep in updated_dependencies:
                print(f" - {dep}")
        
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")


def check_requirements(setup_file='requirements.txt', installed_now=[]):
    if not os.path.exists(setup_file):
        raise FileNotFoundError(f"File not found: {setup_file}")
    else:
        try:
            # Read the current requirements.txt content
            with open(setup_file, 'r') as file:
                content = file.read().splitlines()
                if "" in content:
                    content.remove("")


            updated_packages = []
            for pkg in installed_now:
                if '-' in pkg and '>=' not in pkg:  # Ensure it's not already using '>='
                    name, version = pkg.split('-', 1)
                    updated_packages.append(f"{name}>={version}")
                else:
                    updated_packages.append(pkg)

            
            # Find packages that are not in the requirements.txt
            missing_packages = [pkg for pkg in updated_packages if pkg not in content]


            if not missing_packages:
                print(f"{tic}requirements.txt is already updated.")
            else:
                # Append the missing packages to requirements.txt
                with open(setup_file, 'a') as file:
                    if content and not content[-1].startswith('\n'):
                        file.write('\n')
                    for pkg in missing_packages:
                        file.write(pkg + '\n')
                        print(f"{tic} Added {pkg} to requirements.txt.")

                print(f"{tic}requirements.txt has been updated.")

                with open(setup_file, 'r') as file:
                    content = file.read().splitlines()
            if "" in content:
                content.remove("")

            return content

        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

# UPDATE PYPROJECT.TOML ===============================================================

import os
import toml

from textPlay.colors import *

def read_toml(file_path):
    with open(file_path, 'r') as f:
        return toml.load(f)

# Update a list of dependencies in the TOML data
def update_dependencies(toml_data, dependencies_to_add):
    # Ensure the 'project' and 'dependencies' keys exist
    if 'project' not in toml_data:
        toml_data['project'] = {}
    
    if 'dependencies' not in toml_data['project']:
        toml_data['project']['dependencies'] = []

    dependencies = toml_data['project']['dependencies']
    
    # Add each dependency from the list if it's not already present
    for dep_to_add in dependencies_to_add:
        dep_name = dep_to_add.split(">=")[0]
        if all(dep_name != dep.split(">=")[0] for dep in dependencies):
            dependencies.append(dep_to_add)
    
    toml_data['project']['dependencies'] = dependencies
    return toml_data

# Write the updated TOML data back to the file
def write_toml(file_path, toml_data):
    with open(file_path, 'w') as f:
        toml.dump(toml_data, f)

# Function to update a list of dependencies in pyproject.toml
def update_toml(file_path='pyproject.toml', dependencies_to_add=None):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    else:
        try:
            if dependencies_to_add is None:
                dependencies_to_add = []
            
            data = read_toml(file_path)
            # print(f"Current dependencies: {data.get('project', {}).get('dependencies', [])}")
            
            updated_data = update_dependencies(data, dependencies_to_add)
            write_toml(file_path, updated_data)
            
            print(f"{GREEN}Updated dependencies:{RESET}")
            for dep in updated_data:
                print(f" - {dep}")

        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")



# CHECK PACKAGE ===============================================================\
import importlib.util

def check_package(package_name):
    """Check if a package is installed."""
    package_spec = importlib.util.find_spec(package_name)
    if package_spec is not None:
        return True
    else:
        return False