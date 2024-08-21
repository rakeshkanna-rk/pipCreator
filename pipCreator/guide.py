from constants import title, author, footer
from textPlay.colors import *

guide_text = f"""Author:{author}

Let's get started!

1.  On first let create the project folder.
    USE: {MAGENTA}pipcreator create <location>{RESET}
    this command will create the project folder in the location specified.

2.  Edit the inner folder files that as same name as the project folder.

3.  Edit the folder as you want and have a {GREEN}__init__.py{RESET} file, to initiate the project.

4.  Also Edit the README.md, setup.py, setup.cfg, pyproject.toml and requirements.txt file.
    for more metadata information and setup details.

5.  Convert the project folder to python package. 
    USE: {MAGENTA}pipcreator convert{RESET}
    this will create the wheel and sdist for the project.

6.  Upload the project folder to pypi. 
    USE: {MAGENTA}pipcreator upload{RESET}
    this will upload the project folder to pypi. 
    this command uses twine. to upload the project folder to pypi.
    {YELLOW}make sure you have an account on https://pypi.org .{RESET}


GitHub  : {BLUE}https://github.com/rakeshkanna-rk/pipCreator{RESET}
PyPI    : {BLUE}https://pypi.org/project/pipcreator/{RESET}

{footer}"""

def guide_learn():
    print(guide_text)