from enum import Enum

class Warning(Enum):
    STRUCTURAL_CHANGE = ("structutal_change", "Changes in the jSON's structure may have been found. Please review this course's diff before running the deploy command.")
    REMOVED_LINES = ("removed_lines", "The only change in this course was removed lines. Please review its diff before running the deploy command.")
    REMOVED_FILES = ("removed_lines", "This course has removed files. Please review its diff before running the deploy command.")

    def __init__(self, value, description):
        self._value_ = value
        self.description = description

    def __eq__(self, other):
        if not isinstance(other, Warning):
            return NotImplemented
        return self._value_ == other._value_

    def __hash__(self):
        return hash(self._value_)

class Command:

    @classmethod
    def _init_for_test(cls, command, warnings):
        """
        Alternate constructor for testing purposes. This method is not
        part of the public API of the class and should only be used
        for tests.
        """
        instance = cls.__new__(cls)
        instance.cmd = command
        instance.warnings = warnings
        return instance
    
    def __init__(self, command):
        self.cmd = command.strip()
        self.warnings = []

    def addWarning(self, warning):
        self.warnings.append(warning)

    def __str__(self):
        return f'Command("{self.cmd}", "{self.warnings}")'

    def __repr__(self):
        return f'Command("{self.cmd}", "{self.warnings}")'
    
    def __eq__(self, other):
        if not isinstance(other, Command):
            return NotImplemented

        return self.cmd == other.cmd and self.warnings == other.warnings

    def __hash__(self):
        return hash((self.cmd), self.warnings)