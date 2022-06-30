"""
Name: Siddhanth Biswas
Date: 28-06-2022
Brief Project Description: # Created both a console program and a Graphical User Interface (GUI) program using Python 3
                                and the Kivy toolkit, for an app to display a Movie Collection. The app is interactive
                                by changing movies from watched and unwatched, and by adding new movies to collection.
                                Each movie also has details like title, year, and category.
GitHub URL: https://github.com/tuggypetu/cp1404practicals/tree/master/u_movie_tracker2
"""


from moviecollection import MovieCollection
from movie import Movie

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty


class MoviesToWatchApp(App):
    """Main program - Kivy app to display interactive Movie Collection list"""
    status_output = StringProperty()
    current_sort = StringProperty()
    num_watched = StringProperty()
    sort_tags = ListProperty()
    movie_coll = MovieCollection()

    def build(self):
        """Build Kivy GUI"""
        Window.size = (900, 500)
        self.title = "Movies to Watch 2.0"
        self.root = Builder.load_file("app.kv")
        self.sort_tags = ["Title", "Year", "Category", "Watched"]
        self.load_movies()
        self.current_sort = self.sort_tags[0]
        return self.root

    def change_sort(self, sort_code):
        """ handle change of spinner selection, output result to label widget """
        self.movie_coll.sort(sort_code)
        self.current_sort = sort_code
        self.root.ids.movie_box.clear_widgets()
        self.create_widgets()
        self.num_watched = f"To watch: {self.movie_coll.num_unwatched()}   Watched: {self.movie_coll.num_watched()}"

    def check_movie(self, title_text, year_text, category_text):
        """Error check for add movie inputs"""
        if title_text == '' or year_text == '' or category_text == '':
            self.status_output = "All fields must be completed"
        try:
            year_text = int(year_text)
        except ValueError:
            self.status_output = "Please enter a valid number for year"
        else:
            if category_text.title() not in ['Action', 'Comedy', 'Documentary', 'Drama', 'Fantasy', 'Thriller']:
                self.status_output = "Please enter a valid category: Action, Comedy, Documentary, Drama, Fantasy, " \
                                     "Thriller"
            elif title_text.title() in list(self.root.ids.keys()):
                self.status_output = "Movie already exists in list. Try adding another movie."
            else:
                self.movie_coll.add_movie(Movie((title_text.title()), year_text, category_text.title(), False))
                self.status_output = "Movie added!"
                self.change_sort(self.current_sort)

    def add_mov(self, title_text, year_text, category_text):
        """Add the movie"""
        self.movie_coll.add_movie(Movie((title_text.title()), year_text, category_text.title(), False))
        self.status_output = "Movie added!"
        self.change_sort(self.current_sort)

    def clear_inputs(self):
        """Clear text input fields"""
        self.root.ids.title_input.text, self.root.ids.year_input.text, self.root.ids.category_input.text = '', '', ''

    def load_movies(self):
        """load movies from file"""
        self.movie_coll.load_movies("movies.csv")

    def create_widgets(self):
        """Create the movie widgets"""
        for i, mov in enumerate(self.movie_coll.movies):
            temp_button = Button(text=str(mov))
            temp_button.bind(on_release=self.show_widget_status)
            self.root.ids.movie_box.add_widget(temp_button)
            self.root.ids[mov.title] = temp_button
            self.root.ids[mov.title].background_color = (0, 1, 0, 1) if mov.watched is False else (1, 0, 0, 1)

    def show_widget_status(self, mov):
        """Show the status of the widgets and changed watched and unwatched"""
        mov_title = list(self.root.ids.keys())[list(self.root.ids.values()).index(mov)]
        watch_str = ''
        for movie in self.movie_coll.movies:
            if movie.title in mov.text:
                if movie.watched is False:
                    movie.mark_watched()
                    mov.background_color = (1, 0, 0, 1)
                    mov.text = str(movie)
                else:
                    watch_str = 'not '
                    movie.mark_unwatched()
                    mov.background_color = (0, 1, 0, 1)
                    mov.text = str(movie)
        self.num_watched = f"To watch: {self.movie_coll.num_unwatched()}   Watched: {self.movie_coll.num_watched()}"
        self.status_output = f"You have {watch_str}watched {mov_title}"

    def on_stop(self):
        """Save movies on ending program"""
        self.movie_coll.save_movies()
        print("Movies saved :)\nApp ended.")


if __name__ == '__main__':
    MoviesToWatchApp().run()
