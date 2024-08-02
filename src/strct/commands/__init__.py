# src/strct/commands/__init__.py

from pathlib import Path
import sys

def commands_handler(script_dir):
    from .version import get_version
    from .add import add_new_template
    from .delete import delete_template
    from .list import list_templates
    from .help import help
    from .create_structure import create_structure
    from .git import handle_git_operation

    template_dir = script_dir / 'templates'

    if not template_dir.exists():
        try:
            template_dir.mkdir()
        except PermissionError:
            print("Permission denied to create 'templates' directory.")
            return
     
    if len(sys.argv) < 2:
        help()
        return

    command = sys.argv[1].lower()

    if command == 'help':
        help()
    elif command == 'list':
        list_templates(script_dir)
    elif command == 'add':
        if len(sys.argv) < 4:
            print("Usage: strct add <template_name> <source_path>")
            return
        template_name = sys.argv[2]
        source_path = Path(sys.argv[3])
        add_new_template(script_dir, template_name, source_path)
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: strct delete <template_name>")
            return
        template_name = sys.argv[2]
        delete_template(script_dir, template_name)
    elif command == 'version':
        print(f"strct {get_version()}")
    elif command == 'git':
        if len(sys.argv) < 4:
            print("Usage: strct git <template_name> <operation> [args]")
            return
        template_name = sys.argv[2]
        operation = sys.argv[3]
        args = sys.argv[4:]
        handle_git_operation(script_dir, template_name, operation, *args)
    else:
        # Check if the command is a valid template name for Git operations
        if (template_dir / command).is_dir() and len(sys.argv) > 2 and sys.argv[2].lower() == 'git':
            # This is a Git operation on a template
            template_name = command
            operation = sys.argv[3] if len(sys.argv) > 3 else None
            args = sys.argv[4:]
            handle_git_operation(script_dir, template_name, operation, *args)
        else:
            # Assume it's a structure type
            structure_type = command
            if len(sys.argv) >= 3:
                destination_path = Path(sys.argv[2])
                if not destination_path.is_absolute():
                    destination_path = Path.cwd() / destination_path
            else:
                destination_path = Path.cwd()

            destination_path.mkdir(parents=True, exist_ok=True)
            create_structure(script_dir, structure_type, destination_path)