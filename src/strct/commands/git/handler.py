# src/strct/commands/git/handler.py

import subprocess
from pathlib import Path
from typing import List, Optional
from datetime import datetime

class GitHandler:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path

    def _run_git_command(self, command: List[str]) -> subprocess.CompletedProcess:
        try:
            return subprocess.run(["git"] + command, cwd=self.repo_path, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Git command failed: {e.stderr.strip()}")
            raise

    def init(self) -> bool:
        """Initialize a Git repository."""
        try:
            self._run_git_command(["init"])
            print(f"Initialized Git repository in {self.repo_path}")
            return True
        except subprocess.CalledProcessError:
            return False

    def add_gitignore(self, template: str = "Python") -> bool:
        """Add a .gitignore file to the repository."""
        gitignore_path = self.repo_path / ".gitignore"
        if gitignore_path.exists():
            print(".gitignore already exists. Skipping.")
            return True

        try:
            url = f"https://raw.githubusercontent.com/github/gitignore/master/{template}.gitignore"
            subprocess.run(["curl", "-o", ".gitignore", url], cwd=self.repo_path, check=True, capture_output=True)
            print(f"Added .gitignore file for {template}")
            return True
        except subprocess.CalledProcessError:
            print(f"Failed to add .gitignore for {template}")
            return False

    def add(self, files: List[str] = ["."], update: bool = False) -> bool:
        """Add file(s) to the Git staging area."""
        command = ["add"] + (["--update"] if update else []) + files
        try:
            self._run_git_command(command)
            print(f"Added files to staging: {', '.join(files)}")
            return True
        except subprocess.CalledProcessError:
            return False

    def commit(self, message: str) -> bool:
        """Commit staged changes."""
        try:
            self._run_git_command(["commit", "-m", message])
            print(f"Committed changes: {message}")
            return True
        except subprocess.CalledProcessError:
            return False
        
    def log(self, num_entries: Optional[int] = None, oneline: bool = False) -> None:
        """Show the commit logs."""
        command = ["log"]
        if oneline:
            command.append("--oneline")
        if num_entries is not None:
            command.append(f"-n{num_entries}")

        try:
            result = self._run_git_command(command)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving git log: {e.stderr}")

    def branch(self, name: Optional[str] = None, delete: bool = False) -> bool:
        """Create, list, or delete branches."""
        command = ["branch"]
        if delete:
            command.extend(["-d", name])
        elif name:
            command.append(name)

        try:
            result = self._run_git_command(command)
            if not name and not delete:
                print("Branches:")
                print(result.stdout)
            elif delete:
                print(f"Deleted branch: {name}")
            else:
                print(f"Created branch: {name}")
            return True
        except subprocess.CalledProcessError:
            return False

    def checkout(self, branch: str, new_branch: bool = False) -> bool:
        """Checkout a branch."""
        command = ["checkout"]
        if new_branch:
            command.append("-b")
        command.append(branch)

        try:
            self._run_git_command(command)
            print(f"Checked out branch: {branch}")
            return True
        except subprocess.CalledProcessError:
            return False

    def remote(self, name: str, url: Optional[str] = None, remove: bool = False) -> bool:
        """Add, remove, or list remotes."""
        command = ["remote"]
        if remove:
            command.extend(["remove", name])
        elif url:
            command.extend(["add", name, url])
        else:
            command.extend(["get-url", name])

        try:
            result = self._run_git_command(command)
            if not url and not remove:
                print(f"Remote URL for {name}: {result.stdout.strip()}")
            elif remove:
                print(f"Removed remote: {name}")
            else:
                print(f"Added remote {name}: {url}")
            return True
        except subprocess.CalledProcessError:
            return False

    def push(self, remote: str = "origin", branch: str = "main", set_upstream: bool = False) -> bool:
        """Push changes to a remote repository."""
        command = ["push"]
        if set_upstream:
            command.append("--set-upstream")
        command.extend([remote, branch])

        try:
            self._run_git_command(command)
            print(f"Pushed to {remote}/{branch}")
            return True
        except subprocess.CalledProcessError:
            return False

    def pull(self, remote: str = "origin", branch: str = "main") -> bool:
        """Pull changes from a remote repository."""
        try:
            self._run_git_command(["pull", remote, branch])
            print(f"Pulled from {remote}/{branch}")
            return True
        except subprocess.CalledProcessError:
            return False

    def status(self) -> str:
        """Show the working tree status."""
        try:
            result = self._run_git_command(["status"])
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error getting status: {e.stderr}"

def setup_template_git(path: Path, add_gitignore: bool = False, gitignore_template: str = "Python") -> bool:
    """Set up a Git repository for a template with initial commit."""
    git = GitHandler(path)
    
    if git.init():
        if add_gitignore:
            git.add_gitignore(gitignore_template)
        if git.add() and git.commit("init repo"):
            print("Git repository set up successfully for the template.")
            return True
    
    print("Failed to set up Git repository for the template.")
    return False

def update_template_git(path: Path) -> bool:
    """Update the Git repository for a template."""
    git = GitHandler(path)
    
    try:
        status_output = git.status()
        print(f"Git status before update:\n{status_output}")

        if git.add():
            commit_message = f"Update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            if git.commit(commit_message):
                print("Template Git repository updated successfully.")
                return True
            else:
                print("No changes to commit.")
                return True
        else:
            print("Failed to add files to Git.")
            return False
    except Exception as e:
        print(f"Error updating Git repository: {e}")
        return False