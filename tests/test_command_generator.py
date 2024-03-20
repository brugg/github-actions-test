import unittest
from automation.command_generator import CommandGenerator
from automation.data.change import *
from automation.data.command import *

class TestCommandGenerator(unittest.TestCase):

    def __assert_cmds(self, expected_cmds: list[Command], generated_cmds: list[Command]):
        self.assertEqual(len(expected_cmds), len(generated_cmds))
        
        for expected_command in expected_cmds:
            cmd_found = False

            for command in generated_cmds:
                if expected_command == command:
                    cmd_found = True
            self.assertTrue(cmd_found, f"expected cmd:\n     {expected_command}\nis different from generated cmd:\n     {command}")

    def test_generate_cmds_with_structural_changes(self):
        changes = [ 
            Change._init_for_test(
                "courses/virtual-reality-c/course.json",
                ChangeFileType.COURSE_JSON,
                ChangeGitStatus.MODIFIED,
                ChangeType.ADDED_LINES,
                ChangePosition.MIDDLE
            )
        ]

        commandGenerator = CommandGenerator()
        generated_commands = commandGenerator.generate_commands(changes)
		
        expected_commands = [
            Command._init_for_test("sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-c --environment demo --allow-demo", {Warning.STRUCTURAL_CHANGE})
        ]

        self.__assert_cmds(expected_commands, generated_commands)

    def test_generate_cmds_with_removed_lines(self):
        changes = [ 
            Change._init_for_test(
                "courses/virtual-reality-c/course.json",
                ChangeFileType.COURSE_JSON,
                ChangeGitStatus.MODIFIED,
                ChangeType.REMOVED_LINES,
                ChangePosition.END
            )
        ]

        commandGenerator = CommandGenerator()
        generated_commands = commandGenerator.generate_commands(changes)
		
        expected_commands = [
            Command._init_for_test("sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-c --environment demo --allow-demo", {Warning.REMOVED_LINES})
        ]

        self.__assert_cmds(expected_commands, generated_commands)

    def test_generate_cmds_with_removed_files(self):
        changes = [ 
            Change._init_for_test(
                "courses/virtual-reality-c/course.json",
                ChangeFileType.COURSE_JSON,
                ChangeGitStatus.REMOVED,
                ChangeType.STRUCTURAL_OR_CONTENT_CHANGES,
                ChangePosition.END
            )
        ]

        commandGenerator = CommandGenerator()
        generated_commands = commandGenerator.generate_commands(changes)
		
        expected_commands = [
            Command._init_for_test("sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-c --environment demo --allow-demo", {Warning.REMOVED_FILES, Warning.STRUCTURAL_CHANGE})
        ]

        self.__assert_cmds(expected_commands, generated_commands)

    def test_generate_cmds_with_added_lines_at_end(self):
        changes = [ 
            Change._init_for_test(
                "courses/virtual-reality-c/course.json",
                ChangeFileType.COURSE_JSON,
                ChangeGitStatus.ADDED,
                ChangeType.ADDED_LINES,
                ChangePosition.END
            )
        ]

        commandGenerator = CommandGenerator()
        generated_commands = commandGenerator.generate_commands(changes)
		
        expected_commands = [
            Command._init_for_test("sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-c --environment demo --allow-demo", set())
        ]

        self.__assert_cmds(expected_commands, generated_commands)

    def test_generate_cmds_with_with_added_assets(self):
        changes = [ 
            Change._init_for_test(
                "courses/virtual-reality-c/course.json",
                ChangeFileType.COURSE_JSON,
                ChangeGitStatus.ADDED,
                ChangeType.ADDED_LINES,
                ChangePosition.END
            ),
            Change._init_for_test(
                "courses/virtual-reality-c/projects/lost-treasure/assets/program/5-turning-in-the-treasures/give-the-player-clues-5.mp4",
                ChangeFileType.PROJECT_ASSET,
                ChangeGitStatus.ADDED,
                None,
                None
            )
        ]

        commandGenerator = CommandGenerator()
        generated_commands = commandGenerator.generate_commands(changes)
		
        expected_commands = [
            Command._init_for_test("sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-c --environment demo --allow-demo --project lost-treasure", set())
        ]

        self.__assert_cmds(expected_commands, generated_commands)
            
    def test_generate_cmds_with_with_added_assets(self):
        changes = [ 
            Change._init_for_test(
                "courses/virtual-reality-c/course.json",
                ChangeFileType.COURSE_JSON,
                ChangeGitStatus.ADDED,
                ChangeType.ADDED_LINES,
                ChangePosition.END
            ),
            Change._init_for_test(
                "courses/virtual-reality-c/projects/lost-treasure/assets/program/5-turning-in-the-treasures/give-the-player-clues-5.mp4",
                ChangeFileType.PROJECT_ASSET,
                ChangeGitStatus.ADDED,
                None,
                None
            ),
            Change._init_for_test(
                "courses/virtual-reality-c/projects/lost-treasure/project.json",
                ChangeFileType.PROJECT_JSON,
                ChangeGitStatus.MODIFIED,
                ChangeType.ADDED_LINES,
                ChangePosition.MIDDLE
            )
        ]

        commandGenerator = CommandGenerator()
        generated_commands = commandGenerator.generate_commands(changes)
		
        expected_commands = [
            Command._init_for_test("sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-c --environment demo --allow-demo --project lost-treasure", {Warning.STRUCTURAL_CHANGE})
        ]

        self.__assert_cmds(expected_commands, generated_commands)

if __name__ == '__main__':
    unittest.main()