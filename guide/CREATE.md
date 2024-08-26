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

**Command:**
```bash
pipc create <file_name>
```

**Example:**
```bash
pipc create README.md
```

**What Happens:**
- A `README.md` file or any other template file is created in your project directory.
- The file may include a basic template with for project description, installation instructions, and usage examples, which you can then customize.



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
