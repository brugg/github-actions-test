import unittest
from unittest.mock import patch, MagicMock
from automation.deploy_changes import DeployChanges
import json

class TestDeployChanges(unittest.TestCase):

    # @patch('automation.detect_changes.Github')
    # def setUp(self, mock_github):
    #     # Assuming GitHubClient is initialized within DetectChanges,
    #     # and it uses Github() from PyGithub.
    #     # Mock the entire GitHub client used by DetectChanges.
    #     self.mock_github_client = MagicMock()
    #     mock_github.return_value.get_repo.return_value = self.mock_github_client

    #     # Initialize DetectChanges with the mocked GitHub client
    #     self.detector = DeployChanges(self.mock_github_client)

    def test_analyze_changes_with_mock_json(self):
    #     # Load the mock comparison data from the JSON file
    #     with open('tests/mock_data/v24.03.06-v24.03.13.json', 'r') as file:
    #         mock_data = json.load(file)

    #     # Convert each file change in the mock data into a MagicMock object
        mocked_files = []
    #     for file_change in mock_data['files']:
    #         mocked_file = MagicMock()
    #         mocked_file.filename = file_change['filename']
    #         mocked_file.status = file_change['status']
    #         mocked_files.append(mocked_file)

    #     # Mock the get_comparison method to return an object
    #     # that has a 'files' attribute set to our list of MagicMock objects
    #     mock_comparison = MagicMock()
    #     mock_comparison.files = mocked_files
    #     self.mock_github_client.get_comparison.return_value = mock_comparison
		
    #     # Now you can call analyze_changes and perform your tests
    #     new_files, changed_files, removed_files = self.detector.analyze_changes()

    #     expected_number_of_changed_files = 23
    #     expected_number_of_new_files = 99
    #     expected_number_of_removed_files = 0
        
    #     # Check categorization
    #     self.assertEqual(len(new_files), expected_number_of_new_files)
    #     self.assertEqual(len(changed_files), expected_number_of_changed_files)
    #     self.assertEqual(len(removed_files), expected_number_of_removed_files)


if __name__ == '__main__':
    unittest.main()
