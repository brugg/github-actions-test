class CurriculumChange:
    def __init__(self, action, course_name, changed_file=None):
        self.action = action
        self.course_name = course_name
        self.changed_file = changed_file

class Course:
    def __init__(self, name):
        self.name = name
        self.projects = []
        self.changed_files = []

    def add_project(self, project):
        # Check if project already exists, if not add it
        if not any(p.name == project.name for p in self.projects):
            self.projects.append(project)

    def get_project(self, project_name):
        # Find project in list, or return None
        for project in self.projects:
            if project.name == project_name:
                return project
        return None

class Project:
    def __init__(self, name):
        self.name = name
        self.changed_paths = []