# src/strct/commands/help.py

def help():
    print("Usage: strct <command> [args]")
    print("\nCommands:")
    print("  <structure_type> [destination_path]  Create a new project structure")
    print("  list                                 List available templates")
    print("  add <template_name> <source_path>    Add a new template")
    print("  delete <template_name>               Delete an existing template")
    print("  version                              Show the current version of STRCT")
    print("  help                                 Show this help message")
    print("  git <template_name> <operation> [args] Perform Git operations on a template")
    print("\nGit Operations:")
    print("  init                                 Initialize a new Git repository")
    print("  add <file1> [file2 ...]              Add file(s) to the Git staging area")
    print("  commit <message>                     Commit staged changes")
    print("  branch [name]                        List branches or create a new branch")
    print("  checkout <branch>                    Switch to a different branch")
    print("  remote <name> <url>                  Add a new remote repository")
    print("  push [remote] [branch]               Push changes to a remote repository")
    print("  pull [remote] [branch]               Pull changes from a remote repository")
    print("  status                               Show the working tree status")
    print("  log [-n<number>] [--oneline]         Show commit logs")
    print("\nExamples:")
    print("  strct python-flask my_project        Create a new Flask project structure")
    print("  strct add my_template ./existing_project  Add a new template")
    print("  strct git my_template status         Check Git status of a template")
    print("  strct git my_template log -n5 --oneline  Show last 5 commits in one-line format")