"""Person class"""


class Person:
    def __init__(self, first_name="", last_name="", age=0):
        """Initialise"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """return string"""
        return f"Age of {self.first_name} {self.last_name}: {self.age}"

    def __lt__(self, other):
        """Less than, used for sorting Persons - by age."""
        return self.age < other.age

