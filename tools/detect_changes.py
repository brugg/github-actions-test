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
    # print(f"Analyzing JSON diff: {diff}")

def extract_course_and_project_info(filename):
    """
    Extracts course name, project name (if applicable), and file type from the given filename string.
    
    Example filename: "courses/data-science-and-ai-a-practice-problems/projects/1.1_fortune-teller-practice-problem-1/assets/error.png"
    """
    parts = filename.split('/')
    course_name = None
    project_name = None
    file_type = None

    # Check if the filename follows the expected structure
    if len(parts) > 2 and parts[0] == 'courses':
        course_name = parts[1]  # Extract the course name part        
        if 'projects' in parts:
            project_index = parts.index('projects')
            if len(parts) > project_index + 1:
                project_name = parts[project_index + 1]  # Extract project name
                if 'assets' in parts:
                    file_type = 'project_asset'
                elif 'project.json' in parts:
                    file_type = 'project_json'
                else:
                    file_type = 'undentified'
        elif 'assets' in parts:
            file_type = 'course_asset'
    
    return course_name, project_name, file_type

def categorize_change(file):
    """
    Analyze the file's path and content changes to categorize the change.
    """
    print("-------")
    print(f"file.filename: {file.filename}")

    course_name, project_name, file_type = extract_course_and_project_info(file.filename)
    
    change_summary = {
        "path": file.filename,
        "filename": file.filename.split('/')[-1],
        "course_name": course_name,
        "project_name": project_name,
        "file_type": file_type,
        "action": file.status  # 'added', 'removed', or 'modified'
    }

    # Categorize file based on its status and store it in the corresponding list
    if file.status == 'added':
        new_files.append(change_summary)
    elif file.status == 'removed':
        removed_files.append(change_summary)
    else:  # Assuming 'modified' for any other status
        changed_files.append(change_summary)

    # path_parts = file.filename.split('/')
    # if 'assets' in path_parts:
    #     if 'projects' in path_parts:
    #         print(f"Asset {file.status} to project '{project_name}'")
    #         # if file.status == 'added':
    #         #     print(f"New asset added: {file.filename}")
    #         # elif file.status == 'removed':
    #         #     print(f"Asset removed: {file.filename}")
    #         # else:
    #         #     print(f"Asset updated: {file.filename}")
    #     else:
    #         print(f"Asset {file.status} to course '{course_name}'")
    # elif 'projects' in path_parts:
    #     if file.status == 'added':
    #         print(f"New project added: {file.filename}")
    #     elif file.status == 'removed':
    #         print(f"Project removed: {file.filename}")
    #     else:
    #         print(f"Project updated: {file.filename}")
    #         parse_json_diff(file.patch)
    # elif 'courses' in path_parts:
    #     if file.status == 'added':
    #         print(f"New course added: {file.filename}")
    #     elif file.status == 'removed':
    #         print(f"Course removed: {file.filename}")
    #     else:
    #         print(f"Course updated: {file.filename}")
    #         parse_json_diff(file.patch)

def print_changes(title, changes):
    print(title)
    for change in changes:
        print(json.dumps(change, indent=4))
        print()  # Adds an extra newline for better separation between elements

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

# Define dictionaries to store categorized changes
new_files = []
changed_files = []
removed_files = []

# Analyze file changes
for file in comparison.files:
    categorize_change(file)

# After file changes are categorized, use the function to print them
print_changes("New Files:", new_files)
print("---")
print_changes("Changed Files:", changed_files)
print("---")
print_changes("Removed Files:", removed_files)
print("---")

print("---")
print(" ")
print(f"comparison: {comparison}")
print(" ")
print("---")