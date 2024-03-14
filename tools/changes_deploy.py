import argparse
from data.curriculum_change import *

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("-changes", "--changes", required=True, help="Git changes")
    parser.add_argument("-env", "--environment", required=True, help="Environment (demo, dev, prod)")
    return parser.parse_args()

def parse_data_to_objects(data):
    courses_dict = {}
    
    for line in data.strip().split("\n"):
        parts = line.split()
        if len(parts) < 2 or not parts[1].startswith("courses/"):
            continue  # Skip irrelevant lines

        action, path = parts[0], parts[1]
        path_components = path.split('/')
        course_name = path_components[1]

        # Initialize course if not exists
        if course_name not in courses_dict:
            courses_dict[course_name] = Course(course_name)

        course = courses_dict[course_name]

        # Change directly in the course (e.g., course.json)
        if len(path_components) == 3 and path_components[2] == "course.json":
            course.changed_files.append(CurriculumChange(action, course_name, path))
            continue

        # Changes within projects
        if len(path_components) > 3 and path_components[2] == "projects":
            project_name = path_components[3]
            project = course.get_project(project_name)

            # If project doesn't exist, initialize and add it to the course
            if project is None:
                project = Project(project_name)
                course.add_project(project)
            
            project.changed_paths.append('/'.join(path_components[3:]))

    # Convert dictionary to list of courses for easier handling outside this function
    courses_list = list(courses_dict.values())

    return courses_list

def main():
    args = parse_arguments()

    escaped_changes = args.changes.replace(" ", "\s")
    courses = parse_data_to_objects(args.changes)

    for course in courses:
        print(f"Course: {course.name}")
        projects_arguments = ""
        for project in course.projects:
            # print(f"  Project: {project.name}, Changed Paths: {', '.join(project.changed_paths)}")
            projects_arguments += f"--project {project.name} "
        
        cmd = f"sh deploy-course-to-environment.sh --course {course.name} --environment demo {projects_arguments}"
        print(cmd)