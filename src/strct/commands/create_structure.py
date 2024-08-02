# src/strct/commands/create_structure.py

from pathlib import Path
from ..utilities.general import handle_structure
from .git.handler import setup_template_git

def create_structure(script_dir, structure_type, base_path, git_init=False, gitignore_template="Python"):
    """
    Create project structure based on the given type and optionally initialize Git.

    Args:
        script_dir (Path): The directory where STRCT is installed.
        structure_type (str): The type of project structure to create.
        base_path (Path): The path where the new project structure will be created.
        git_init (bool, optional): Whether to initialize a Git repository. Defaults to False.
        gitignore_template (str, optional): The template to use for .gitignore. Defaults to "Python".

    Returns:
        None
    """
    template_path = script_dir / 'templates' / structure_type

    if template_path.exists():
        # Create the project structure
        handle_structure(script_dir, structure_type, base_path)
        print(f"{structure_type.capitalize()} project structure created successfully in {base_path}")

        # Initialize Git repository if requested
        if git_init:
            if setup_template_git(base_path, add_gitignore=True, gitignore_template=gitignore_template):
                print(f"Git repository initialized in {base_path}")
            else:
                print("Failed to initialize Git repository")
    else:
        print(f"Structure type '{structure_type}' is not supported yet.")
        print("Available templates:")
        templates = [d.name for d in (script_dir / 'templates').iterdir() if d.is_dir()]
        print(", ".join(templates))

