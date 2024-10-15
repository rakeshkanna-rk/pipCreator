### 1. **Creating a New Python Project**
To create a new Python project, use the `pipc create <project_name>` command. You can specify the `<project_name>` command followed by your desired project name. This will generate a new directory with the specified project name, you can then use the `pipc create ./` command to create files in current directory. Then answer the following questions to create a new project.

**Structure:**
```
my_project/
│
├── my_project/
│   ├── __init__.py
│   └── main.py
│
├── test/ (test folder is optional)
│   └── test.py
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
└── pyproject.toml (or) setup.py
```

**Command:**
```bash
pipc create <project_name>
```

**Example:**
```bash
pipc create my_project
```

**What Happens:**
- A new directory named `my_project` is created.
- Inside this directory, basic files and folders like `__init__.py`, `main.py`, `README.md`, `LICENSE`, `requirements.txt`, `.gitignore`, and `pyproject.toml` or `setup.py`  and an optional `test/test.py` folder are created.

### 2. **Creating Template Files**
To Create template files, use the `pipc create <file_name>` command. This will create a new template file in your project directory. Available templates are `setup.py`, `pyproject.toml`, `README.md`, `.gitignore`, `requirements.txt`, and `test.py`.
You can also create non-template files by flaging `--file` option and create folder with `--folder`.
**Command:**
```bash
pipc create <file_name>
```

```bash
pipc create <file_name> --file
```

```bash
pipc create <folder_name> --folder
```

**Example:**
```bash
pipc create README.md
```

```bash
pipc create file.py --file
```

```bash
pipc create app --folder
```

**What Happens:**
- A `README.md` file or any other template file is created in your project directory.
- The file may include a basic template with for project description, installation instructions, and usage examples, which you can then customize.
- You can also create non-template files by flaging `--file` option and create folder with `--folder` option.

### 3. **Setting Up a Virtual Environment**
A virtual environment is essential for managing dependencies and ensuring your project runs in a controlled environment. You can create a virtual environment using `pipc` as well.

**Command:**
```bash
pipc create venv
```

### For Activating a Virtual Environment
**For Windows CMD**
```bash
venv\Script\activate.bat
```

**For Linux/Mac Bash**
```bash
source venv/bin/activate
```

### For Deactivating a Virtual Environment

**For Windows CMD**
```bash
venv\Script\deactivate.bat
```

**For Linux/Mac Bash**
```bash
deactivate
```

**What Happens:**
- A virtual environment named `venv` is created inside your project directory.
- This environment is isolated from your global Python environment, allowing you to install project-specific packages without affecting other projects.

### 4. **Creating a Project**

```bash
PS E:\> pipc create Project

        PIP CREATOR v0.1.0

Creating project @ E:\

Enter project name [Project]
Enter a description for your project My new project
Enter keywords for your project new project first example
Enter author name Rakesh Kanna
Enter author email rakeshkanna0108@gmail.com
Enter license for your project [MIT] 
Any dependencies for your project MonoCipher textPlay

Do you want to create a test folder? (y/n) [Y] 
Do you want to initialize git? (y/n) [Y] 
Reinitialized existing Git repository in E:\Projects\.git
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
√ Project/__init__.py created successfully.
√ Project/main.py created successfully.
√ Project/test/test.py created successfully.

How to Use/Activate virtual environment
   use: pipc guide --see on-venv

√ All files created successfully.

Project/
│
├── Project/
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

         cd Project

Happy Coding!
```