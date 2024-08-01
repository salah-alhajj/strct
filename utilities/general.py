import os
from pathlib import Path
from .copy import copy_template
import os
from pathlib import Path
from .copy import copy_template

def handle_structure(structure_type: str, base_path):
    script_dir = Path(__file__).parent.parent  # Go up one level to reach the STRCT directory
    template_path = script_dir / 'templates' / structure_type
    
    if copy_template(template_path, base_path):
        print(f"{structure_type.capitalize()} project structure created successfully in {base_path}")
    else:
        print(f"Failed to create {structure_type.capitalize()} project structure.")
