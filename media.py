#!/usr/bin/env python2.7.13  # shebang line for the used Python version

# need to import webbrowser to be able to show the movie trailer

import webbrowser


class Movie():
    """This ia a class that displays movie information"""
    # init procedure to store the instance variables
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, release_date, duration):
        self.title = movie_title                    # instance variable for movie title
        self.storyline = movie_storyline            # instance variable for movie storyline
        self.poster_image_url = poster_image        # instance variable for poster image
        self.trailer_youtube_url = trailer_youtube  # instance variable for youtube trailer
        self.release_date = release_date            # instance variable for the release date
        self.duration = duration                    # instance variable for duration

    # procedure to show the youtube trailer in a webbrowser

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
