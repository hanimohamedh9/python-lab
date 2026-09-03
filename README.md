My Python Lab Project

Part A - Command Breakdown
The cd ~ command navigates to the home directory, and mkdir python_lab creates the project workspace. Running cd python_lab enters the project directory, while mkdir src, tests, docs builds the subdirectories. The New-Item command creates the Python scripts (main.py, utils.py, config.py) inside src. Using Set-Content applies output redirection to write "My Python Lab Project" directly into docs/README.md without launching a text editor. Finally, tree /F recursively displays the directory hierarchy and its nested contents.

Why Structure Matters

Structuring projects into src, tests, and docs establishes a clean, modular layout that supports project growth. Isolating source code inside src prevents import paths from breaking and keeps executable scripts organized. Dedicated tests folders keep automated testing code separate so test dependencies aren't packaged into production releases. Storing project documentation in docs gives collaborators direct access to instructions without searching through codebase files.
part b
What .gitignore does: It tells Git which files or directories to intentionally ignore and exclude from version control tracking so they don't get accidentally uploaded to GitHub.
​Why the file patterns matter:
​Python Cache (_pycache_/ & *.pyc): These are temporary compiled bytecode files generated automatically by Python, keeping the repository clean and preventing unnecessary machine-specific cache files from cluttering version control.
​Environment files (.env): These store sensitive configuration data like API keys and passwords, preventing accidental public exposure of private credentials.
​What commit history reveals: It provides a chronological timeline of a project's development, showing who made changes, when they were made, and specific messages explaining why modifications or additions were implemented over time.