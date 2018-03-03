# -*- coding: utf-8 -*-


class Movie():
    """
    Movie.
    """
    def __init__(self, title, story_line, poster_image_url, trailer_url):
        """ Initialize a movie instance.
        :param title: movie title
        :param story_line: movie story line
        :param poster_image_url: url of movie poster
        :param trainler_url: url of movie trailer
        """
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url

