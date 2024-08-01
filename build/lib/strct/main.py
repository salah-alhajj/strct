import os
import sys
from pathlib import Path
from .commands import commands_handler

def main():
    user_home = Path(os.path.expanduser("~"))
    
    # Create a .strct directory in the user's home folder if it doesn't exist
    strct_dir = user_home / ".strct"
    strct_dir.mkdir(exist_ok=True)
    commands_handler(strct_dir)

if __name__ == "__main__":
    main()