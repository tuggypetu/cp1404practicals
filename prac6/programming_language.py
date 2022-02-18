"""Class for characteristics of programming languages"""


class ProgrammingLanguage:
    """"""
    def __init__(self, name="", typing="", reflection=True, year=0):
        """Initialise"""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns string"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if language typing is dynamic or not"""
        if self.typing == "Dynamic":
            return True
        else:
            return False
