import os
import subprocess
from pathlib import Path

def get_install_dir():
    return Path.home() / "AppData" / "Local" / "STRCT"

def add_to_path(install_dir):
    print("Adding STRCT to PATH (Windows)")
    try:
        subprocess.run(["setx", "PATH", f"%PATH%;{install_dir}"], check=True)
        print("STRCT added to PATH successfully.")
    except subprocess.CalledProcessError:
        print("Failed to add STRCT to PATH. You may need to add it manually.")

def create_symlink(install_dir):
    # Windows doesn't typically use symlinks, so we'll create a .bat file in a directory that's in the PATH
    script_dir = Path(os.environ.get("USERPROFILE")) / "AppData" / "Local" / "Microsoft" / "WindowsApps"
    script_path = script_dir / "strct.bat"
    target_path = install_dir / "strct.bat"
    
    print(f"Creating/updating batch file at {script_path}")
    try:
        script_content = f'@echo off\n"{target_path}" %*'
        script_path.write_text(script_content)
        print("Batch file created successfully.")
    except PermissionError:
        print("Failed to create batch file. You may need to run the installer with administrator privileges.")

def post_install_message(install_dir):
    print(f"STRCT installed successfully in {install_dir}")
    print("Please restart your command prompt to use STRCT.")