from pathlib import Path

from ..utilities.general import handle_structure


def create_structure(script_dir,structure_type, base_path):
    """Create project structure based on the given type."""
    template_path = script_dir / 'templates' / structure_type

    if template_path.exists():
        handle_structure(script_dir,structure_type, base_path)
    else:
        print(f"Structure type '{structure_type}' is not supported yet.")
        print("Available templates:")
        templates = [d.name for d in (script_dir / 'templates').iterdir() if d.is_dir()]
        print(", ".join(templates))
