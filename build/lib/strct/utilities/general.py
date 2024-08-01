import os
from pathlib import Path
import os
from pathlib import Path

from ..commands.copy import copy_template

def handle_structure(script_dir,structure_type: str, base_path):
    template_path = script_dir / 'templates' / structure_type
    
    if copy_template(template_path, base_path):
        print(f"{structure_type.capitalize()} project structure created successfully in {base_path}")
    else:
        print(f"Failed to create {structure_type.capitalize()} project structure.")
