from pipcreator.constants import author, footer, title
from textPlay.colors import *

import webbrowser

def code(text):
    return f"{BRIGHT_BLUE}pipc{MAGENTA}{text}{RESET}"

guide_text = f"""{title}
Let's get started!

What PIP CREATOR can do?

1.  Create a new python project using {code(" create <project_name>")}. 
    Created project consists of README.md, .gitignore, requirements.txt, 
    project_name/main.py project_name/main.py, test/test.py(optional) and one setup file i.e., setup.py or pyproject.toml.
    Use create command to create a template file using {code(" create readme.md")}.
    Available templates are setup.py, pyproject.toml, README.md, .gitignore, requirements.txt.
    Use create command to create a virtual environment using {code(" create venv")}.
    For more information, use {code(" guide --see on-create")}.

2.  Convert a python project to distribution file using {code(" convert")}.
    You can also upgrade your project version on converting the project.
    Automatically analyze your project and upgrade your project version number you want.
    For more information, use {code(" guide --see on-convert")}.

3.  Upload your project to PyPI using {code(" upload")}.
    For more information, use {code(" guide --see on-upload")}.

4.  Install your project dependency using {code(" install <package_name>")}.
    You can also install requirements.txt dependencies using {code(" install requirements.txt")}.
    You can also update your project dependency on installation.
    For more information, use {code(" guide --see on-install")}.

5.  Uninstall your project dependency using {code(" uninstall <package_name>")}.
    You can also uninstall requirements.txt dependencies using {code(" install requirements.txt")}.
    For more information, use {code(" guide --see on-uninstall")}.

6.  Update your project dependency using {code(" update <package_name>")}.
    You can also update requirements.txt dependencies using {code(" install requirements.txt")}.
    For more information, use {code(" guide --see on-update")}.

7.  Search for your project dependency using {code(" search <package_name>")}.
    For more information, use {code(" guide --see on-search")}.

8.  List all your installed packages using {code(" list")}.
    For more information, use {code(" guide --see on-list")}.

9.  Git Commit and Push your project using {code(" commit -m <message>")}.
    Git Clone your project using {code(" clone <repo_url> <path_optional>")}.
    For more information, use {code(" guide --see on-git")}.

GitHub  : {BLUE}https://github.com/rakeshkanna-rk/pipCreator{RESET}
PyPI    : {BLUE}https://pypi.org/project/pipCreator/{RESET}

{footer}"""


def guide_learn():
    print(guide_text)

import webbrowser

def web_guide(see):
    see = see[3:].upper()
    valid_topics = ["VENV", "CREATE", "CONVERT", "UPLOAD", "PACKAGE", "GIT"]
    
    if see in valid_topics:
        webbrowser.open(f"https://github.com/rakeshkanna-rk/pipCreator/tree/main/guide/{see}.md")
    else:
        print(f"{RED}Invalid topic{RESET}")

# Example usage
web_guide(see="on-create")
