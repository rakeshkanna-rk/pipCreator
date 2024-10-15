<p align="center">

<img src="https://raw.githubusercontent.com/rakeshkanna-rk/pipCreator/refs/heads/main/logo/logoDark.png#gh-dark-mode-only" width="200px">

<img src="https://raw.githubusercontent.com/rakeshkanna-rk/pipCreator/refs/heads/main/logo/logoLight.png#gh-light-mode-only" width="200px">

</p>

<h1 align="center"> PIP CREATOR v0.1.0</h1>

PIP CREATOR is a command-line interface tool designed to streamline the process of creating, testing, converting, and uploading Python modules to PyPI (Python Package Index). With this tool, developers can easily generate all necessary files and folders for their Python modules and apps, edit or update existing code, create test suites, convert their code to distribution formats, and seamlessly upload their packages to PyPI.

> [!WARNING]
> This tool is in **BETA** / **DEVELOPMENT** stage. It may contain bugs or incomplete features at current versions `v0.1.0b1`.

## Features

1. **File Generation**: Automatically create all necessary files and folders for a Python module, including `.gitignore`, `LICENSE`, `README.md`, `setup.py`, `setup.cfg`, `pyproject.toml`, `requirements.txt`, `test/test.py`(optional), `project/__init__.py`, and `project/main.py`. Pre-written code is provided in the generated files, allowing users to easily edit or update the code according to their requirements. [GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/CREATE.md)

2. **Plugins**: Add additional functionality to the generated files by using plugins. [Check Available Plugins](https://github.com/rakeshkanna-rk/pipCreator/blob/main/PLUGINS.md).

3. **Conversion to Distribution Formats**: Convert Python modules to distribution formats (`bdist`, `sdist`, `wheel`) with automatic validation of necessary files. [GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/CONVERT.md)

4. **PyPI Upload**: Seamlessly upload Python packages to PyPI using Twine. [GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/UPLOAD.md)

5. **CLI Guide**: Access a short guide within the CLI on how to create, convert, and upload Python libraries. [GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/)

6. **Install Python Packages**: Install Python packages using `pipc`. Managing dependencies is crucial for maintaining a Python project with better visuals. [GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

7. **Uninstall Python Packages**: Uninstall Python packages using `pipc`. Managing dependencies is crucial for maintaining a Python project with better visuals. [GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

8. **Update Python Packages**: Update Python packages using `pipc`. Managing dependencies is crucial for maintaining a Python project with better visuals. [GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

9. **Search Python Packages**: Search for Python packages using `pipc`. Searching python packages in CLI with better visuals. [GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

10. **List Python Packages**: List all Python packages installed. [GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

11. **Show Package Info**: Show package info with clear visuals. [GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)


## Installation

```bash
pip install pipCreator
```

## Usage

### Creating Python Module Files and Folders

```bash
pipc create <location>
```

This command will generate all necessary files and folders for a Python module in the specified `<location>`. The generated files include `.gitignore`, `LICENSE`, `README.md`, `setup.py`, `setup.cfg`, `pyproject.toml`, `requirements.txt`, `project/__init__.py`, and `project/main.py`.

[CREATE GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/CREATE.md)

### Converting to Distribution Formats

```bash
pipc convert
```

Convert the Python module to distribution formats (`bdist`, `sdist`, `wheel`). This command automatically checks whether all necessary files exist before conversion.

[CONVERT GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/CONVERT.md)

### Uploading to PyPI

```bash
pipc upload
```

Upload the Python package to PyPI using Twine.

[UPLOAD GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/UPLOAD.md)

---

### Installing Python Packages

```bash
pipc install <package_name>
```

Install Python packages using pip. Managing dependencies is crucial for maintaining a Python project with better visuals.

[PACKAGE GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

### Uninstalling Python Packages

```bash
pipc uninstall <package_name>
```

Uninstall Python packages using pip. Managing dependencies is crucial for maintaining a Python project with better visuals.

[PACKAGE GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

### Updating Python Packages

```bash
pipc update <package_name>
```

Update Python packages using pip. Managing dependencies is crucial for maintaining a Python project with better visuals.

[PACKAGE GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

### Searching Python Packages

```bash
pipc search <package_name>
```

Search for Python packages using pip. Searching python packages in CLI with better visuals.

[PACKAGE GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

### Listing Python Packages

```bash
pipc list
```

List all Python packages installed.

[PACKAGE GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

### Show Package Info

```bash
pipc show <package_name>
```

Show package info with clear visuals.

[PACKAGE GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/PACKAGE.md)

### Plugins

```bash
pipc install <plugin_name> --plugin
```

Install pipc plugins.

[PLUGINS](https://github.com/rakeshkanna-rk/pipCreator/blob/main/PLUGINS.md)

---

### CLI Guide

```bash
pipc guide
```

**for specific topic**

```bash
pipc guide --see on-<topic>
```

Access a short guide within the CLI on how to create, convert, and upload Python libraries.

[GUIDE](https://github.com/rakeshkanna-rk/pipCreator/blob/main/guide/)

---

## Examples

### Creating files on a new project

```bash
PS E:\test\new> pipc create new_project

        PIP CREATOR v0.1.0

Creating project @ E:\test\new

Directory doesn't exist.
Do you like to create the directory? (y/n) [Y] 
√ Directory created successfully.

Enter project name [new_project] 
Enter a description for your project a new python package
Enter keywords for your project new python package
Enter author name Rakesh Kanna
Enter author email rakeshkanna0108@gmail.com
Enter license for your project [MIT]
Any dependencies for your project requests click Fl\ask 

Do you want to create a test folder? (y/n) [Y]
Do you want to initialize git? (y/n) [Y] 
Do you like to create a virtual environment for your dependencies? (y/n) [Y] [venv]

√ Virtual environment created successfully.

Setup Types: setup.py pyproject.toml
● Do you want to create a setup.py file for your project? (y/n)
● Do you want to create a pyproject.toml file for your project? (y/n)
● Do you want to create a setup.py file for your project? (y/n)
● Do you want to create a pyproject.toml file for your project? (y/n) y

√ pyproject.toml created successfully.
√ README.md created successfully.
√ .gitignore created successfully.
√ License created successfully.
√ requirements.txt created successfully.
√ new_project/__init__.py created successfully.
√ new_project/main.py created successfully.
√ new_project/test/test.py created successfully.

How to Use/Activate virtual environment
   use: pipc guide --see on-venv

√ All files created successfully.

new_project/
│
├── new_project/
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
└── pyproject.toml


Your project folder is ready to code.

         cd new_project

Happy Coding!
```

### You can also create in current loaction using

```bash
pipcreator create ./
```

```bash
pipcreator create .
```

### Converting to sdist bdist wheel file

```bash
PS E:\test\new\new_project> pipc convert           

        PIP CREATOR v0.1.0

Converting files will happen @ E:\test\new\new_project
Project name: new_project

√ Folder contains all required files.
√ setup.py found.
Update version number? (y/n) [Y]:
Current version: 0.1.0
Enter new version number: 0.1.1
Updated version:  0.1.1

√ setup.py updated.
Are you sure you want to convert to distribution file? (y/n) [Y]:
Converting files...

√ Files Converted successfully.

Happy Coding!
```

### Uploading your module to PyPI

```bash
PS D:\PyModule> pipcreator upload 

        PIP CREATOR v0.1.0

Uploading files will happen in current directory: D:\PyModule
Project name: PyModule


Make sure you have an account and genrate a API key at https://pypi.org
Are you sure you want to convert to sdist and bdist? [y/n]: y
Folder contains all required files. ✔
This will use twine to upload the package. 

<uploading process>

Package has uploaded/not uploaded as per the twine

Happy Coding!
```

### Guide

```bash
PS E:\test\new> pipc guide 

        PIP CREATOR v0.1.0

Let's get started!

What PIP CREATOR can do?

1.  Create a new python project using pipc create <project_name>.
    Created project consists of README.md, .gitignore, requirements.txt,
    project_name/main.py project_name/main.py, test/test.py(optional) and one setup file i.e., setup.py or pyproject.toml.
    Use create command to create a template file using pipc create readme.md.
    Available templates are setup.py, pyproject.toml, README.md, .gitignore, requirements.txt.
    Use create command to create a virtual environment using pipc create venv.
    For more information, use pipc guide --see on-create.

2.  Convert a python project to distribution file using pipc convert.
    You can also upgrade your project version on converting the project.
    Automatically analyze your project and upgrade your project version number you want.
    For more information, use pipc guide --see on-convert.

3.  Upload your project to PyPI using pipc upload.
    For more information, use pipc guide --see on-upload.

4.  Install your project dependency using pipc install <package_name>.
    You can also install requirements.txt dependencies using pipc install requirements.txt.
    You can also update your project dependency on installation.
    For more information, use pipc guide --see on-package.

5.  Uninstall your project dependency using pipc uninstall <package_name>.
    You can also uninstall requirements.txt dependencies using pipc install requirements.txt.
    For more information, use pipc guide --see on-package.

6.  Update your project dependency using pipc update <package_name>.
    You can also update requirements.txt dependencies using pipc install requirements.txt.
    For more information, use pipc guide --see on-package.

7.  Search for your project dependency using pipc search <package_name>.
    For more information, use pipc guide --see on-package.

8.  List all your installed packages using pipc list.
    For more information, use pipc guide --see on-package.

9.  Git Commit and Push your project using pipc commit -m <message>.
    Git Clone your project using pipc clone <repo_url> <path_optional>.
    For more information, use pipc guide --see on-git.

GitHub  : https://github.com/rakeshkanna-rk/pipCreator
PyPI    : https://pypi.org/project/pipCreator/

Happy Coding!
```

## Contributing

Contributions are welcome! Please feel free to submit [issues](https://github.com/rakeshkanna-rk/pipCreator/issues) or [pull requests](https://github.com/rakeshkanna-rk/pipCreator/pulls).

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

## Author Details

Author  : **Rakesh Kanna**  
Mail    : [rakeshkanna0108@gmail.com](mailto:rakeshkanna0108@gmail.com)  
Github  : [@rakeshkanna-rk](https://github.com/rakeshkanna-rk)  
GitHub  : [PipCreator](https://github.com/rakeshkanna-rk/pipCreator/)  
PyPI    : [PipCreator](https://pypi.org/project/PipCreator/)  
