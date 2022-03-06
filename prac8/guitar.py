"""Guitar class"""

AGE_CALC = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar Class"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        """Return string"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return age"""
        return AGE_CALC - self.year

    def is_vintage(self):
        """Return T is more than 50 years old(vintage)"""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year
