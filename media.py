# Class movie: class that creates a movie with some attributes
import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, director, info):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.info = info

    def show_trailer(self):
        """show_trailer() doc:
        That function open a browser to show a trailer
        """
        webbrowser.open(self.trailer_youtube_url)
