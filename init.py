
import sys
from pathlib import Path
from commands import commands_handler
from utilities import *




    
if __name__ == "__main__":
    script_dir = Path(__file__).parent
    commands_handler(script_dir)