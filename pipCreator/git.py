import subprocess
from textPlay.colors import *

def git_commit_and_push(commit_message: str):
    """
    Commits and pushes changes to a Git repository.

    Parameters:
    commit_message (str): The commit message to use.
    """

    try:
        # Stage all changes
        print(f"{BLUE}Staging changes...")
        subprocess.check_call(["git", "add", "."])
        print(f"{GREEN}Changes staged.")

        # Commit the changes
        print(f"{BLUE}Committing changes...")
        subprocess.check_call(["git", "commit", "-m", commit_message])
        print(f"{GREEN}Changes committed with message:", commit_message)

        # Push the changes to the remote repository
        print(f"{BLUE}Pushing changes to the remote repository...")
        subprocess.check_call(["git", "push"])
        print(f"{GREEN}Changes pushed successfully.")
        print(RESET)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Git command failed. Please check the error message above for details.")



def git_clone_repository(repo_url: str, destination_folder=None):
    """
    Clones a Git repository.

    Parameters:
    repo_url (str): The URL of the Git repository to clone.
    destination_folder (str): The destination folder where the repository should be cloned.
                              If None, the repository will be cloned into a folder with the same name as the repo.
    """

    try:
        # Prepare the clone command
        command = ["git", "clone", repo_url]
        if destination_folder:
            command.append(destination_folder)

        # Clone the repository
        print(f"Cloning repository from {repo_url}...")
        subprocess.check_call(command)
        print(f"Repository cloned successfully into {destination_folder or repo_url.split('/')[-1]}")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Git clone failed. Please check the error message above for details.")

