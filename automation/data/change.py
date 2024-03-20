import re
from enum import Enum

class Change:

    def __str__(self):
        return f'\nChange: \n     "{self.path}",\n     "{self.file_type}",\n     "{self.git_status}",\n     "{self.change_type}",\n     "{self.change_position}"\n)'

    @classmethod
    def _init_for_test(cls, path, file_type, git_status, change_type, change_position):
        """
        Alternate constructor for testing purposes. This method is not
        part of the public API of the class and should only be used
        for tests.
        """
        instance = cls.__new__(cls)

        course_name, project_name, file_type = instance.extract_course_and_project_info(path)

        instance.path = path
        instance.filename = path.split('/')[-1]
        instance.course_name = course_name
        instance.project_name = project_name
        instance.file_type = file_type
        instance.git_status = git_status
        instance.change_type = change_type
        instance.change_position = change_position
        return instance

    def __init__(self, github_client, file):
        self.github_client = github_client

        course_name, project_name, file_type = self.extract_course_and_project_info(file.filename)

        self.path = file.filename
        self.filename = file.filename.split('/')[-1]
        self.course_name = course_name
        self.project_name = project_name
        self.file_type = file_type
        self.git_status = ChangeGitStatus.from_string(file.status)
        self.change_type = None
        self.change_position = None
        
        # We only need the change type for course.json and project.json files.
        if (self.file_type == ChangeFileType.COURSE_JSON or self.file_type == ChangeFileType.PROJECT_JSON):
            self.change_type = ChangeType.resolve_change_type(file.patch)
            raw_file = self.github_client.download_raw_file(file.contents_url)
            if (raw_file != None):
                self.change_position = ChangePosition.resolve_change_position(file.patch, raw_file)                
    

    def extract_course_and_project_info(self, filePath):
        parts = filePath.split('/')
        course_name = None
        project_name = None
        file_type = None

        if len(parts) > 2 and parts[0] == 'courses':
            course_name = parts[1]
            if 'projects' in parts:
                project_index = parts.index('projects')
                if len(parts) > project_index + 1:
                    project_name = parts[project_index + 1]
                    if 'assets' in parts:
                        file_type = ChangeFileType.PROJECT_ASSET
                    elif 'project.json' in parts:
                        file_type = ChangeFileType.PROJECT_JSON
            elif 'assets' in parts:
                file_type = ChangeFileType.COURSE_ASSET
            elif 'course.json' in parts:
                file_type = ChangeFileType.COURSE_JSON
            elif 'vocabulary.json' in parts:
                file_type = ChangeFileType.VOCABULARY
            elif 'feedback.json' in parts:
                file_type = ChangeFileType.FEEDBACK
        
        return course_name, project_name, file_type
    

class ChangeGitStatus(Enum):
    MODIFIED = "modified"
    ADDED = "added"
    REMOVED = "removed"

    def __init__(self, value):
        self._value_ = value

    def from_string(value):
        return ChangeGitStatus._value2member_map_.get(value, None)

class ChangeFileType(Enum):
    COURSE_ASSET = ("course_asset", "Used when the file is a course's asset.")
    COURSE_JSON = ("course_json", "Used when the file is the course's jSON.")
    PROJECT_ASSET = ("project_asset", "Used when the file is a project's asset.")
    PROJECT_JSON = ("project_json", "Used when the file is the project's jSON.")
    VOCABULARY = ("vocabulary", "Used when the file is the vocabulary.json.")
    FEEDBACK = ("feedback", "Used when the file is the feedback.json.")
    
    def __init__(self, value, description):
        self._value_ = value
        self.description = description

class ChangeType(Enum):
    STRUCTURAL_OR_CONTENT_CHANGES = 'structural_or_content_changes' # Any change different from added and removed
    ADDED_LINES = 'new_lines'
    REMOVED_LINES = 'removed_lines'

    @staticmethod
    def resolve_change_type(patch):
        added = any(line.startswith('+') and not line.startswith('+++') for line in patch.split('\n'))
        removed = any(line.startswith('-') and not line.startswith('---') for line in patch.split('\n'))
        
        if added and removed:
            return ChangeType.STRUCTURAL_OR_CONTENT_CHANGES
        elif added:
            return ChangeType.ADDED_LINES
        elif removed:
            return ChangeType.REMOVED_LINES
        
        return None

class ChangedBlock:
    def __init__(self, start_line, end_line):
        self.start_line = start_line
        self.end_line = end_line

    def __repr__(self):
        return f"ChangedBlock(start_line={self.start_line}, end_line={self.end_line})"
    
class ChangePosition(Enum):
    MIDDLE = ("changes_middle", "Used when file's changes were at the start or in the middle of the document.")
    END = ("changes_end", "Used when file's changes were at the end of the document.")

    def __init__(self, value, description):
        self._value_ = value
        self.description = description
    
    @staticmethod
    def resolve_change_position(patch, file_content):
        file_lines = file_content.split('\n')

        # Regex pattern to extract added lines from the patch.
        hunk_header_pattern = re.compile(r'\@\@ -\d+,\d+ \+(\d+),(\d+) \@\@')
        changed_blocks = []

        # Extract start and end lines of added sections.
        for match in hunk_header_pattern.finditer(patch):
            start_line, line_count = map(int, match.groups())
            end_line = start_line + line_count - 1
            changed_blocks.append(ChangedBlock(start_line, end_line))

        # Determine if added lines are at the end, excluding closing marks.
        def is_change_at_end(file_lines, changed_blocks):
            non_change_content = False
            closing_pattern = re.compile(r'^\s*[\}\]]*\s*$')
            
            # Iterate backwards through the file to find the first non-closing mark line.
            for line_num in range(len(file_lines), 0, -1):
                if not closing_pattern.match(file_lines[line_num - 1]):
                    break

            # Check if changed blocks are at the end or interspersed with unchanged content.
            for block in reversed(changed_blocks):
                if block.end_line < line_num:
                    non_change_content = True
                    break
                line_num = block.start_line - 1

            return ChangePosition.END if not non_change_content else ChangePosition.MIDDLE

        return is_change_at_end(file_lines, changed_blocks)