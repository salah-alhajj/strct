import os
import subprocess
from pathlib import Path

def get_install_dir():
    return Path.home() / ".local" / "share" / "strct"

def get_shell_config_file():
    home = Path.home()
    if "ZSH_VERSION" in os.environ:
        return home / ".zshrc"
    else:
        return home / ".bashrc"

def add_to_path(install_dir):
    config_file = get_shell_config_file()
    print(f"Adding STRCT to PATH in {config_file}")
    with open(config_file, "a") as f:
        f.write(f'\nexport PATH="$PATH:{install_dir}"\n')

def create_symlink(install_dir):
    symlink_path = Path("/usr/local/bin/strct")
    target_path = install_dir / "strct"
    print(f"Creating/updating symlink at {symlink_path}")
    try:
        if symlink_path.is_symlink() and symlink_path.resolve() == target_path:
            print("Symlink already exists and is correct.")
            return
        
        if symlink_path.exists():
            symlink_path.unlink()
        
        symlink_path.symlink_to(target_path)
        print("Symlink created successfully.")
    except PermissionError:
        print("Symlink creation/update requires sudo privileges.")
        try:
            subprocess.run(["sudo", "ln", "-sf", str(target_path), str(symlink_path)], check=True)
            print("Symlink created/updated successfully with sudo.")
        except subprocess.CalledProcessError:
            print("Failed to create/update symlink even with sudo. Please check your permissions.")

def post_install_message(install_dir):
    print(f"STRCT installed successfully in {install_dir}")
    print("Please restart your terminal or run 'source ~/.zshrc' (for Zsh) or 'source ~/.bashrc' (for Bash) to use STRCT.")