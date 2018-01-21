# -*- coding: utf-8 -*-


from fresh_tomatoes import open_movies_page
from media import Movie
import json
import sys
import os


class EntertainmentCenter():
    def __init__(self, movies_data_path=None):
        self.movies = []
        if movies_data_path and os.path.exists(movies_data_path):
            with open(movies_data_path, 'r') as f:
                for m in json.load(f):
                    title = m['title']
                    story_line = m['story_line']
                    poster_image_url = m['poster_image_url']
                    trailer_url = m['trailer_url']
                    if sys.version < '3':
                        title = title.encode('utf8')
                        story_line = story_line.encode('utf8')
                        poster_image_url = poster_image_url.encode('utf8')
                        trailer_url = trailer_url.encode('utf8')
                    movie = Movie(title,story_line,poster_image_url,trailer_url)
                    self.movies.append(movie)
        else:
            print('Please use a json file which contains movies data to start!')
    
    def play(self):
        open_movies_page(self.movies)

if __name__ == '__main__':
    e_center = EntertainmentCenter('data/movies.json')