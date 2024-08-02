# src/strct/commands/git_operations.py

from pathlib import Path
from .handler import GitHandler

def handle_git_operation(script_dir: Path, template_name: str, operation: str, *args):
    template_path = script_dir / 'templates' / template_name
    
    if not template_path.exists():
        print(f"Template '{template_name}' does not exist.")
        return

    if not (template_path / '.git').is_dir():
        print(f"The template '{template_name}' is not a Git repository.")
        return

    git = GitHandler(template_path)
    
    if not hasattr(git, operation):
        print(f"Unknown Git operation: {operation}")
        return

    try:
        if operation == 'log':
            num_entries = None
            oneline = False
            for arg in args:
                if arg.startswith('-n'):
                    try:
                        num_entries = int(arg[2:])
                    except ValueError:
                        print(f"Invalid number of entries: {arg}")
                        return
                elif arg == '--oneline':
                    oneline = True
            log_output = git.log(num_entries=num_entries, oneline=oneline)
            print(log_output)
        else:
            getattr(git, operation)(*args)
    except Exception as e:
        print(f"Git operation failed: {e}")