import os
import sys
import shutil
from pathlib import Path
from commands.version import get_version, VERSION

def get_os_module():
    if sys.platform == "darwin":
        from installer import macos as os_module
    elif sys.platform == "win32":
        from installer import windows as os_module
    else:  # Assume Linux for any other platform
        from installer import linux as os_module
    return os_module

def copy_strct_files(install_dir):
    current_dir = Path(__file__).parent
    print(f"Copying STRCT files to {install_dir}")
    for item in current_dir.iterdir():
        if item.is_file():
            shutil.copy2(item, install_dir)
        elif item.is_dir() and item.name not in [".git", "__pycache__"]:
            shutil.copytree(item, install_dir / item.name, dirs_exist_ok=True)

def create_executable(install_dir):
    if sys.platform == "win32":
        script_path = install_dir / "strct.bat"
        script_content = f'@echo off\npython "{install_dir / "init.py"}" %*'
    else:
        script_path = install_dir / "strct"
        script_content = f'#!/bin/bash\npython3 "{install_dir / "init.py"}" "$@"'
    
    print(f"Creating STRCT executable at {script_path}")
    with open(script_path, "w") as f:
        f.write(script_content)
    
    if sys.platform != "win32":
        script_path.chmod(0o755)  # Make the script executable on Unix-like systems

def check_existing_installation(install_dir):
    version_file = install_dir / "version.py"
    if version_file.exists():
        sys.path.insert(0, str(install_dir))
        from version import VERSION as installed_version
        sys.path.pop(0)
        return installed_version
    return None

def main():
    print(f"Installing STRCT version {VERSION} on {sys.platform}")
    os_module = get_os_module()
    
    install_dir = os_module.get_install_dir()
    
    existing_version = check_existing_installation(install_dir)
    if existing_version:
        if existing_version >= VERSION:
            print(f"STRCT version {existing_version} is already installed and up to date.")
            choice = input("Do you want to force a reinstall? (y/N): ").lower()
            if choice != 'y':
                print("Installation cancelled.")
                return
        else:
            print(f"Updating STRCT from version {existing_version} to {VERSION}")
    
    install_dir.mkdir(parents=True, exist_ok=True)
    
    copy_strct_files(install_dir)
    create_executable(install_dir)
    os_module.add_to_path(install_dir)
    os_module.create_symlink(install_dir)
    os_module.post_install_message(install_dir)

if __name__ == "__main__":
    main()