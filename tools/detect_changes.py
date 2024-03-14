from github import Github
import os
import json

def parse_json_diff(diff):
    """
    Placeholder function to analyze and categorize the JSON diff.
    You might want to use a diff library or write custom logic
    to compare JSON structures and content.
    """
    # This is a simplified example. You'll need to replace this with actual logic
    # to parse and interpret the JSON diffs meaningfully.
    print(f"Analyzing JSON diff: {diff}")

def categorize_change(file):
    """
    Analyze the file's path and content changes to categorize the change.
    """
    print("-------")
    print(f"file.filename: {file.filename}")
    path_parts = file.filename.split('/')
    if 'courses' in path_parts:
        if file.status == 'added':
            print(f"New course added: {file.filename}")
        elif file.status == 'removed':
            print(f"Course removed: {file.filename}")
        else:
            print(f"Course updated: {file.filename}")
            parse_json_diff(file.patch)
    elif 'projects' in path_parts:
        if file.status == 'added':
            print(f"New project added: {file.filename}")
        elif file.status == 'removed':
            print(f"Project removed: {file.filename}")
        else:
            print(f"Project updated: {file.filename}")
            parse_json_diff(file.patch)
    elif 'assets' in path_parts:
        if file.status == 'added':
            print(f"New asset added: {file.filename}")
        elif file.status == 'removed':
            print(f"Asset removed: {file.filename}")
        else:
            print(f"Asset updated: {file.filename}")


# Initialize GitHub API client
g = Github(os.getenv('GITHUB_TOKEN'))
repo = g.get_repo(os.getenv('REPOSITORY_NAME'))

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
    categorize_change(file)
