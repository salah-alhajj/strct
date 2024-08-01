
import os
import sys
from pathlib import Path
from utilities import *

def create_structure(structure_type, base_path):
    """Create project structure based on the given type."""
    script_dir = Path(__file__).parent
    template_path = script_dir / 'templates' / structure_type

    if template_path.exists():
        handle_structure(structure_type, base_path)
    else:
        print(f"Structure type '{structure_type}' is not supported yet.")
        print("Available templates:")
        templates = [d.name for d in (script_dir / 'templates').iterdir() if d.is_dir()]
        print(", ".join(templates))

def list_templates():
    script_dir = Path(__file__).parent
    templates = [d.name for d in (script_dir / 'templates').iterdir() if d.is_dir()]
    print("Available structure types:")
    print(", ".join(templates))
def main():
    if len(sys.argv) < 2:
        help()
        return

    command = sys.argv[1].lower()

    if command == 'help':
        help()
    elif command == 'list':
        list_templates()
    elif command == 'add':
        if len(sys.argv) < 4:
            print("Usage: strct add <template_name> <source_path>")
            return
        template_name = sys.argv[2]
        source_path = Path(sys.argv[3])
        add_new_template(template_name, source_path)
    else:
        # Assume it's a structure type
        structure_type = command
        if len(sys.argv) >= 3:
            destination_path = Path(sys.argv[2])
            if not destination_path.is_absolute():
                destination_path = Path.cwd() / destination_path
        else:
            destination_path = Path.cwd()

        destination_path.mkdir(parents=True, exist_ok=True)
        create_structure(structure_type, destination_path)

if __name__ == "__main__":
    main()