from github import Github, Auth
import requests

class GitHubClient:
    def __init__(self, token, repo_name):
        self.token = token
        self.github = Github(auth=Auth.Token(token))
        self.repo = self.github.get_repo(repo_name)
    
    def get_comparison(self):
        tags = list(self.repo.get_tags())
        latest_tag = tags[0].name
        previous_tag = tags[1].name if len(tags) > 1 else None

        if previous_tag:
            comparison = self.repo.compare(previous_tag, latest_tag)
        else:
            comparison = self.repo.compare("initial_commit_sha", latest_tag)

        print(f"comparison: {comparison}")
        return comparison

    def download_raw_file(self, contents_url):
        # Set up the headers with your GitHub token for authorization
        headers = {
            "Authorization": f"bearer {self.token}",
            "Accept": "application/vnd.github.v3.raw"
        }

        # Make the GET request to download the file content
        try:
            response = requests.get(contents_url, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses

            return response.text
        except requests.RequestException as e:
            print(f"Error downloading file: {e}")
            return None