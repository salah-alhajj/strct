from pathlib import Path
from strct.commands.copy import copy_template

def add_new_template(script_dir,template_name: str, source_path: Path):
    template_dir = script_dir / 'templates'
    new_template_path = template_dir / template_name

    if new_template_path.exists():
        print(f"Template '{template_name}' already exists. Please choose a different name.")
        return

    if not source_path.exists():
        print(f"Source directory '{source_path}' does not exist.")
        return

    if copy_template(source_path, new_template_path):
        print(f"New template '{template_name}' added successfully.")
    else:
        print(f"Failed to add new template '{template_name}'.")
