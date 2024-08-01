
import shutil

def copy_template(source_path, destination_path):
    """Copy template directory to destination."""
    if not source_path.exists():
        print(f"Error: Source directory '{source_path}' not found.")
        return False

    try:
        shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
        print(f"Successfully copied from {source_path} to {destination_path}")
        return True
    except Exception as e:
        print(f"Error copying template: {e}")
        return False