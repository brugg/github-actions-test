import unittest
import os
import json
from unittest.mock import patch, MagicMock
from automation.data.change import Change, ChangeFileType, ChangeType, ChangePosition, ChangeGitStatus
from automation.clients.github_client import GitHubClient

class TestChange(unittest.TestCase):

    def setUp(self):
        GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
        REPOSITORY_NAME = "Hello-World-CS/curriculum"
        self.github_client = GitHubClient(GITHUB_TOKEN, REPOSITORY_NAME)

    # Diff: https://github.com/Hello-World-CS/curriculum/compare/v24.03.06...v24.03.13
    # courses/virtual-reality-c/course.json
    def test_change_creation_with_new_lines_at_middle(self):
        with open('tests/mock_data/data/virtual-reality-c_course.json', 'r') as f:
            json_str = json.load(f)
        
        mocked_file = MagicMock()
        mocked_file.filename = json_str['filename']
        mocked_file.status = json_str['status']
        mocked_file.contents_url = json_str['contents_url']
        mocked_file.patch = json_str['patch']    
        change = Change(self.github_client, mocked_file)

        print(change)
        
        self.assertEqual("course.json", change.filename)
        self.assertEqual("virtual-reality-c", change.course_name)
        self.assertEqual(None, change.project_name)
        self.assertEqual(ChangeGitStatus.MODIFIED, change.git_status)
        self.assertEqual(ChangeFileType.COURSE_JSON, change.file_type)
        self.assertEqual(ChangeType.ADDED_LINES, change.change_type)
        self.assertEqual(ChangePosition.MIDDLE, change.change_position)
    
    # Diff: https://github.com/Hello-World-CS/curriculum/compare/v24.03.06...v24.03.13
    # courses/data-science-and-ai-a-practice-problems/course.json
    def test_change_creation_with_new_lines_at_end(self):
        with open('tests/mock_data/data/data-science-and-ai-a-practice-problems_course.json', 'r') as f:
            json_str = json.load(f)
        
        mocked_file = MagicMock()
        mocked_file.filename = json_str['filename']
        mocked_file.status = json_str['status']
        mocked_file.contents_url = json_str['contents_url']
        mocked_file.patch = json_str['patch']    
        change = Change(self.github_client, mocked_file)
        
        self.assertEqual("course.json", change.filename)
        self.assertEqual("data-science-and-ai-a-practice-problems", change.course_name)
        self.assertEqual(None, change.project_name)
        self.assertEqual(ChangeGitStatus.MODIFIED, change.git_status)
        self.assertEqual(ChangeFileType.COURSE_JSON, change.file_type)
        self.assertEqual(ChangeType.ADDED_LINES, change.change_type)
        self.assertEqual(ChangePosition.END, change.change_position)

    # Diff: https://github.com/Hello-World-CS/curriculum/compare/v24.03.06...v24.03.13
    # courses/data-science-and-ai-a-practice-problems/projects/level-4-independent-projects-practice-problem-1/project.json
    def test_change_creation_new_file(self):
        with open('tests/mock_data/data/level-4-independent-projects-practice-problem-1_project.json', 'r') as f:
            json_str = json.load(f)
        
        mocked_file = MagicMock()
        mocked_file.filename = json_str['filename']
        mocked_file.status = json_str['status']
        mocked_file.contents_url = json_str['contents_url']
        mocked_file.patch = json_str['patch']
        change = Change(self.github_client, mocked_file)
        
        self.assertEqual("project.json", change.filename)
        self.assertEqual("data-science-and-ai-a-practice-problems", change.course_name)
        self.assertEqual("level-4-independent-projects-practice-problem-1", change.project_name)
        self.assertEqual(ChangeGitStatus.ADDED, change.git_status)
        self.assertEqual(ChangeFileType.PROJECT_JSON, change.file_type)
        self.assertEqual(ChangeType.ADDED_LINES, change.change_type)
        self.assertEqual(ChangePosition.END, change.change_position)

    # Diff: https://github.com/Hello-World-CS/curriculum/compare/v24.03.06...v24.03.13
    # courses/virtual-reality-b/projects/lost-treasure/assets/program/1-building-the-scene/add-characters-and-animals-1.mp4
    def test_change_new_asset(self):
        with open('tests/mock_data/data/add-characters-and-animals-1_mp4.json', 'r') as f:
            json_str = json.load(f)
        
        mocked_file = MagicMock()
        mocked_file.filename = json_str['filename']
        mocked_file.status = json_str['status']
        mocked_file.contents_url = json_str['contents_url']
        mocked_file.patch = json_str['patch']
        change = Change(self.github_client, mocked_file)
        
        self.assertEqual("add-characters-and-animals-1.mp4", change.filename)
        self.assertEqual("virtual-reality-b", change.course_name)
        self.assertEqual("lost-treasure", change.project_name)
        self.assertEqual(ChangeGitStatus.ADDED, change.git_status)
        self.assertEqual(ChangeFileType.PROJECT_ASSET, change.file_type)
        self.assertEqual(None, change.change_type)
        self.assertEqual(None, change.change_position)

    # Diff: https://github.com/Hello-World-CS/curriculum/compare/v24.03.06...v24.03.13
    # courses/virtual-reality-b/projects/lost-treasure/project.json
    def test_change_with_text_updates_only(self):
        with open('tests/mock_data/data/lost-treasure_project.json', 'r') as f:
            json_str = json.load(f)
        
        mocked_file = MagicMock()
        mocked_file.filename = json_str['filename']
        mocked_file.status = json_str['status']
        mocked_file.contents_url = json_str['contents_url']
        mocked_file.patch = json_str['patch']
        change = Change(self.github_client, mocked_file)
        
        self.assertEqual("project.json", change.filename)
        self.assertEqual("virtual-reality-b", change.course_name)
        self.assertEqual("lost-treasure", change.project_name)
        self.assertEqual(ChangeGitStatus.MODIFIED, change.git_status)
        self.assertEqual(ChangeFileType.PROJECT_JSON, change.file_type)
        self.assertEqual(ChangeType.STRUCTURAL_OR_CONTENT_CHANGES, change.change_type)
        # self.assertEqual(ChangeType.TEXT_UPDATES, change.change_type)
        self.assertEqual(ChangePosition.MIDDLE, change.change_position)

    # Diff: https://github.com/Hello-World-CS/curriculum/compare/v24.02.22...v24.03.06
    # courses/virtual-reality-a/projects/passion-project-level-5/project.json
    def test_change_with_multiple_updates(self):
        with open('tests/mock_data/data/passion-project-level-5_project.json', 'r') as f:
            json_str = json.load(f)
        
        mocked_file = MagicMock()
        mocked_file.filename = json_str['filename']
        mocked_file.status = json_str['status']
        mocked_file.contents_url = json_str['contents_url']
        mocked_file.patch = json_str['patch']
        change = Change(self.github_client, mocked_file)
        
        self.assertEqual("project.json", change.filename)
        self.assertEqual("virtual-reality-a", change.course_name)
        self.assertEqual("passion-project-level-5", change.project_name)
        self.assertEqual(ChangeGitStatus.MODIFIED, change.git_status)
        self.assertEqual(ChangeFileType.PROJECT_JSON, change.file_type)
        self.assertEqual(ChangeType.STRUCTURAL_OR_CONTENT_CHANGES, change.change_type)
        # self.assertEqual(ChangeType.STRUCTURAL_CHANGES, change.change_type) # In the future we will need to identify this
        self.assertEqual(ChangePosition.MIDDLE, change.change_position)
        
    # Diff: https://github.com/Hello-World-CS/curriculum/compare/v24.02.22...v24.03.06
    # courses/virtual-reality-a/projects/picnic-party/project.json
    def test_change_with_different_text_updates(self):
        with open('tests/mock_data/data/picnic-party_project.json', 'r') as f:
            json_str = json.load(f)
        
        mocked_file = MagicMock()
        mocked_file.filename = json_str['filename']
        mocked_file.status = json_str['status']
        mocked_file.contents_url = json_str['contents_url']
        mocked_file.patch = json_str['patch']
        change = Change(self.github_client, mocked_file)
        
        self.assertEqual("project.json", change.filename)
        self.assertEqual("virtual-reality-a", change.course_name)
        self.assertEqual("picnic-party", change.project_name)
        self.assertEqual(ChangeGitStatus.MODIFIED, change.git_status)
        self.assertEqual(ChangeFileType.PROJECT_JSON, change.file_type)
        self.assertEqual(ChangeType.STRUCTURAL_OR_CONTENT_CHANGES, change.change_type)
        # self.assertEqual(ChangeType.TEXT_UPDATES, change.change_type)
        self.assertEqual(ChangePosition.MIDDLE, change.change_position)