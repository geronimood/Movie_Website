#!/usr/bin/env python2.7.13  # shebang line for the used Python version

import fresh_tomatoes   # need to import fresh_tomatoes to redner the HTML page
import media            # need to import media to access the class Movie

# different instances of the class Movie

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        1995, 81)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     2009, 162)

lammbock = media.Movie("Lammbock",
                       "Lammbock ist eine deutsche Filmkomoedie",
                       "http://www.filmposter-archiv.de/filmplakat/2001/lammbock.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=9aSjKzNzc8I",
                       2001, 90)

school_of_rock = media.Movie("School of Rock",
                             "School of Rock is a 2003 musical comedy film",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
                             2003, 108)

matchpoint = media.Movie("Matchpoint",
                         "Match Point ist ein Thriller aus dem Jahr 2005",
                         "https://cdn.traileraddict.com/content/dreamworks-pictures/matchpoint.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=8AAuMrSygno",
                         2005, 119)

ratatouille = media.Movie("Ratatouille",
                          "Ratatouille ist ein US-Animationsfilm",
                          "https://vignette4.wikia.nocookie.net/disney/images/c/c8/Ratatouille_poster.jpg/revision/latest?cb=20130328084644",  # NOQA
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          2007, 111)

# the movies are stored in a list

movies = [toy_story, avatar, lammbock, school_of_rock, matchpoint, ratatouille]


# this calls the open_movies_page procedure
# from the fresh_tomatoes file with the input variable movies

fresh_tomatoes.open_movies_page(movies)
