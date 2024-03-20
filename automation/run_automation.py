import os
from .clients.github_client import GitHubClient
from .deploy_changes import DeployChanges

def main():
    print("Running")

    try:
        GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
        # REPOSITORY_NAME = os.getenv('REPOSITORY_NAME')
        REPOSITORY_NAME = "Hello-World-CS/curriculum"
        
        
        # Check if the environment variables are set
        if not GITHUB_TOKEN or not REPOSITORY_NAME:
            raise ValueError("GITHUB_TOKEN and REPOSITORY_NAME must be set as environment variables.")
        
        github_client = GitHubClient(GITHUB_TOKEN, REPOSITORY_NAME)
        deployChanges = DeployChanges(github_client)
        deployChanges.deploy()

        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("Ended")

if __name__ == "__main__":
    main()
