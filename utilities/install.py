import os
import sys
import shutil
import subprocess
from pathlib import Path

def get_install_dir():
    home = Path.home()
    if sys.platform == "win32":
        return home / "AppData" / "Local" / "STRCT2"
    elif sys.platform == "darwin":
        return home / "Library" / "Application Support" / "STRCT2"
    else:  # Linux and other Unix-like systems
        return home / ".local" / "share" / "strct2"

def get_shell_config_file():
    home = Path.home()
    if sys.platform == "win32":
        return None  # Windows doesn't use shell config files
    elif sys.platform == "darwin":
        if "ZSH_VERSION" in os.environ:
            return home / ".zshrc"
        else:
            return home / ".bash_profile"
    else:  # Linux and other Unix-like systems
        if "ZSH_VERSION" in os.environ:
            return home / ".zshrc"
        else:
            return home / ".bashrc"

def copy_strct_files(install_dir):
    current_dir = Path(__file__).parent
    if not current_dir.exists():
        print("Error: Cannot find STRCT directory.")
        sys.exit(1)
    
    print(f"Copying STRCT files to {install_dir}")
    for item in current_dir.iterdir():
        if item.is_file():
            shutil.copy2(item, install_dir)
            print(f"Copied file: {item.name}")
        elif item.is_dir() and item.name not in [".git", "__pycache__"]:
            shutil.copytree(item, install_dir / item.name, dirs_exist_ok=True)
            print(f"Copied directory: {item.name}")
    
    # Check if builder.py exists in the installation directory
    if not (install_dir / "builder.py").exists():
        print("Error: builder.py not found in the installation directory.")
        print("Contents of installation directory:")
        for item in install_dir.iterdir():
            print(f" - {item.name}")
        sys.exit(1)

def create_executable(install_dir):
    if sys.platform == "win32":
        script_path = install_dir / "strct2.bat"
        script_content = f'@echo off\npython "{install_dir / "builder.py"}" %*'
    else:
        script_path = install_dir / "strct2"
        script_content = f'#!/bin/bash\necho "Executing: python3 \\"{install_dir / "builder.py"}\\" $@"\npython3 "{install_dir / "builder.py"}" "$@"'
    
    print(f"Creating STRCT executable at {script_path}")
    with open(script_path, "w") as f:
        f.write(script_content)
    
    if sys.platform != "win32":
        script_path.chmod(0o755)  # Make the script executable on Unix-like systems

def add_to_path(install_dir):
    if sys.platform == "win32":
        print("Adding STRCT to PATH (Windows)")
        subprocess.run(["setx", "PATH", f"%PATH%;{install_dir}"], check=True)
        os.environ["PATH"] += os.pathsep + str(install_dir)
    else:
        config_file = get_shell_config_file()
        if config_file:
            print(f"Adding STRCT to PATH in {config_file}")
            with open(config_file, "a") as f:
                f.write(f'\nexport PATH="$PATH:{install_dir}"\n')
            os.environ["PATH"] += os.pathsep + str(install_dir)

def create_symlink(install_dir):
    if sys.platform != "win32":
        symlink_path = Path("/usr/local/bin/strct2")
        print(f"Creating symlink at {symlink_path}")
        try:
            symlink_path.symlink_to(install_dir / "strct2")
        except PermissionError:
            print("Symlink creation requires sudo privileges.")
            subprocess.run(["sudo", "ln", "-sf", str(install_dir / "strct2"), str(symlink_path)], check=True)

def update_current_session():
    if sys.platform != "win32":
        shell = os.environ.get("SHELL", "").lower()
        if "zsh" in shell:
            os.system("source ~/.zshrc")
        elif "bash" in shell:
            os.system("source ~/.bashrc")
        print("PATH has been updated for the current session.")
    else:
        print("PATH has been updated. Changes will take effect in new command prompts.")

def check_directory(path):
    print(f"Checking directory: {path}")
    print(f"Exists: {path.exists()}")
    if path.exists():
        print(f"Is directory: {path.is_dir()}")
        print(f"Permissions: {oct(path.stat().st_mode)[-3:]}")
        print("Contents:")
        for item in path.iterdir():
            print(f" - {item.name}")
    else:
        print("Directory does not exist.")
    print()

def main():
    print(f"Installing STRCT2 on {sys.platform}")
    install_dir = get_install_dir()
    
    # Check parent directories
    parent_dirs = list(install_dir.parents)
    parent_dirs.reverse()
    for dir in parent_dirs + [install_dir]:
        check_directory(dir)
    
    try:
        install_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Error creating installation directory: {e}")
        sys.exit(1)
    
    copy_strct_files(install_dir)
    create_executable(install_dir)
    add_to_path(install_dir)
    
    if sys.platform != "win32":
        create_symlink(install_dir)
    
    update_current_session()
    
    print("STRCT2 installation completed.")
    print(f"Installation directory: {install_dir}")
    print("You can now use STRCT2 by typing 'strct2' in your terminal.")
    if sys.platform == "win32":
        print("Note: On Windows, you may need to open a new command prompt to use STRCT2.")
    
    # Final directory check
    print("\nFinal check of installation directory:")
    check_directory(install_dir)

if __name__ == "__main__":
    main()