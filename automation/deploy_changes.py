from .data.change import Change
from .command_generator import *

class DeployChanges:
    def __init__(self, github_client):
        self.github_client = github_client
        self.changes = []
        self.command_generator = CommandGenerator()
    
    def analyze_changes(self):
        changes = []
        
        comparison = self.github_client.get_comparison()

        for file in comparison.files:
            if file.filename.split('/')[0] == 'courses':
                changes.append(Change(self.github_client, file)) 

        return changes

    def deploy(self):
        changes = self.analyze_changes()

        commands = self.command_generator.generate_commands(changes)

        print(f"Commands:")
        for command in commands:
            print(f"{command}\n")
        
        # Return the dictionaries for further use
        return None