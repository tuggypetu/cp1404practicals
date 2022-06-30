"""Class for MovieCollection"""


from operator import itemgetter
from movie import Movie


class MovieCollection(Movie):
    """Class for collection of movies from movie class"""

    def __init__(self, title="", year=0, category="", watched=False, movies=None):
        """Initialise MovieCollection object"""
        super().__init__(title, year, category, watched)
        if movies is None:
            movies = []
        self.movies = movies

    def __str__(self, i=0):
        """Return string for all movies"""
        if not self.movies:
            return super().__str__()
        elif self.movies[i] == self.movies[-1]:
            return str(self.movies[i])
        elif i <= (len(self.movies) - 1):
            return f"{str(self.movies[i])}" + '\n' + self.__str__(i + 1)

    def add_movie(self, add_movie):
        """add a movie to class"""
        self.movies.append(add_movie)

    def num_unwatched(self):
        """Return number of unwatched movies"""
        num_unwatched = 0
        for mov in self.movies:
            num_unwatched += 1 if mov.watched is False else 0
        return num_unwatched

    def num_watched(self):
        """Return number of watched movies"""
        num_watched = 0
        for mov in self.movies:
            num_watched += 1 if mov.watched is True else 0
        return num_watched

    def load_movies(self, filename):
        """Load all movies and its details from file"""
        in_file = open(filename, 'r')
        for line in in_file:
            line = line.strip().split(',')
            watched = line[-1] == "w"
            self.movies.append(Movie(line[0], int(line[1]), line[2], watched))
        in_file.close()

    def save_movies(self):
        """Save all movies in this class into new file"""
        out_file = open("movies_save.csv", 'w')
        for mov in self.movies:
            watch = 'u' if mov.watched is False else 'w'
            out_file.write(f"{mov.title},{mov.year},{mov.category},{watch}\n")
        out_file.close()

    def sort(self, dimension="title"):
        """sort movies based on key"""
        movies_list = []
        for movie in self.movies:
            movies_list.append([movie.title, movie.year, movie.category, movie.watched])
        d_list = ["title", "year", "category", "watched"]
        if dimension.lower() in d_list:
            if dimension.lower() != "title":
                movies_list.sort(key=itemgetter(d_list.index(dimension.lower()), 0))
            else:
                movies_list.sort(key=itemgetter(0))
            new_movies = []
            for mov in movies_list:
                new_movies.append(Movie(mov[0], int(mov[1]), mov[2], mov[3]))
            self.movies = new_movies
        else:
            print("Incorrect key for sort in MovieCollection. Options are: title", "year", "category", "is_watched")
