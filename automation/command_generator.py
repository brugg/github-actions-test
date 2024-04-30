from .data.command import *
from .data.change import *
from .data.curriculum_change import *

from typing import List

class CommandGenerator:
    
# TEST CHANGES
# branch changes

    def generate_commands(self, changes):
        courses = self.__get_courses_list(changes)
        
        commands = []
        for course in courses:
            projects_arguments = ""
            for project in course.projects:
                projects_arguments += f"--project {project.name} "
            
            command = Command(f"sh tools/deploy/deploy-course-to-environment.sh --course {course.name} --environment demo --allow-demo {projects_arguments}")
            command.warnings = course.warnings    
            commands.append(command)

        return commands

    def __get_courses_list(self, changes) -> list[Course]:
        courses_dict = {}

        for change in changes:
            course_name = change.course_name

            # Initialize course if not exists
            if course_name not in courses_dict:
                courses_dict[course_name] = Course(course_name)

            course = courses_dict[course_name]

            if change.project_name:
                project = course.get_project(change.project_name)
                if project is None:
                    project = Project(change.project_name)
                    course.add_project(project)
            
            if change.change_type == ChangeType.STRUCTURAL_OR_CONTENT_CHANGES:
                course.add_warning(Warning.STRUCTURAL_CHANGE)
            elif change.change_type == ChangeType.REMOVED_LINES:
                course.add_warning(Warning.REMOVED_LINES)

            if change.git_status == ChangeGitStatus.REMOVED:
                course.add_warning(Warning.REMOVED_FILES)
            elif change.git_status == ChangeGitStatus.MODIFIED and change.change_position == ChangePosition.MIDDLE:
                course.add_warning(Warning.STRUCTURAL_CHANGE)

            courses_dict[course_name] = course
            
        courses_list = list(courses_dict.values())

        return courses_list