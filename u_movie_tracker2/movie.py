"""Class for Movie"""


class Movie:
    """Class to store movie details"""

    def __init__(self, title="", year=0, category="", watched=False):
        """Initialise movie object"""
        self.title = title
        self.year = year
        self.category = category
        self.watched = watched

    def __str__(self):
        """Return string for movie"""
        watched_string = "not watched" if self.watched is False else "watched"
        return "The {} movie {} released in {} is {}.".format(self.category.lower(), self.title, self.year,
                                                              watched_string)

    def mark_watched(self):
        """Mark movie as watched"""
        self.watched = True

    def mark_unwatched(self):
        """Mark movie as unwatched"""
        self.watched = False
