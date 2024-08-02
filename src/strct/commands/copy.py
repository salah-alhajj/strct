# src/strct/commands/add.py

import shutil
from pathlib import Path
from strct.commands.git.handler import GitHandler, setup_template_git, update_template_git

def copy_template(source_path: Path, destination_path: Path):
    try:
        shutil.copytree(source_path, destination_path, ignore=shutil.ignore_patterns('.git*'), dirs_exist_ok=True)
        print(f"Successfully copied from {source_path} to {destination_path}")
        return True
    except Exception as e:
        print(f"Error copying template: {e}")
        return False

def add_new_template(script_dir, template_name: str, source_path: Path):
    template_dir = script_dir / 'templates'
    new_template_path = template_dir / template_name

    if new_template_path.exists():
        print(f"Template '{template_name}' already exists. Updating existing template.")
        if copy_template(source_path, new_template_path):
            print(f"Template '{template_name}' updated successfully.")
            if (new_template_path / '.git').is_dir():
                if update_template_git(new_template_path):
                    print(f"Git repository updated for template '{template_name}'")
                else:
                    print(f"Failed to update Git repository for template '{template_name}'")
        else:
            print(f"Failed to update template '{template_name}'.")
        return

    if not source_path.exists():
        print(f"Source directory '{source_path}' does not exist.")
        return

    if copy_template(source_path, new_template_path):
        print(f"New template '{template_name}' added successfully.")
        
        # Initialize Git repository for the new template
        use_git = input("Do you want to initialize a Git repository for this template? (y/n): ").lower() == 'y'
        if use_git:
            add_gitignore = input("Do you want to add a .gitignore file? (y/n): ").lower() == 'y'
            gitignore_template = "Python"
            if add_gitignore:
                gitignore_template = input("Enter the GitIgnore template name (default: Python): ") or "Python"
            if setup_template_git(new_template_path, add_gitignore, gitignore_template):
                print(f"Git repository initialized for template '{template_name}'")
            else:
                print(f"Failed to initialize Git repository for template '{template_name}'")
    else:
        print(f"Failed to add new template '{template_name}'.")