import sys
from pathlib import Path
from .commands import commands_handler

def main():
    script_dir = Path(__file__).parent
    commands_handler(script_dir)

if __name__ == "__main__":
    main()