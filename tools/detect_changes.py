from github import Github
import os

# Initialize GitHub API client
g = Github(os.getenv('GITHUB_TOKEN'))
repo = g.get_repo("your_github_username/your_repository_name")

# Get the latest and previous tags (assuming tags are used for releases)
tags = list(repo.get_tags())
latest_tag = tags[0].name
previous_tag = tags[1].name if len(tags) > 1 else None

# Compare two tags if previous exists, else compare with the initial commit
if previous_tag:
    comparison = repo.compare(previous_tag, latest_tag)
else:
    comparison = repo.compare("initial_commit_sha", latest_tag)

# Analyze file changes
for file in comparison.files:
    print(f"File {file.filename} changed")
    # You can extend this to look into the file's patch attribute to analyze changes
    # and classify them as new course, update, etc.

# TODO: Further analysis to categorize changes