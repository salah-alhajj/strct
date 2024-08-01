from pathlib import Path
import shutil


def delete_template(script_dir,template_name):
    """Delete a template from the templates directory."""
    template_path = script_dir / 'templates' / template_name

    if template_path.exists():
        try:
            shutil.rmtree(template_path)
            print(f"Template '{template_name}' has been deleted successfully.")
        except Exception as e:
            print(f"Error deleting template '{template_name}': {e}")
    else:
        print(f"Template '{template_name}' does not exist.")
