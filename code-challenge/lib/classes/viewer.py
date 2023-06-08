class Viewer:
    all =[]
    
    def __init__(self, username):
        self.username = username
        type(self).all.append(self)
    
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if '_username' not in dir(self) and isinstance(username, str) and 6 <= len(username) <= 16:
            self._username = username
        else:
            raise AttributeError('Not from username class')
    
    
    
    
    
    def reviews(self):
        return[review for review in Review.all if review.viewer is self]
    
    def reviewed_movies(self):
        return [review.movie for review in self.reviews()]

    def has_reviewed_movie(self, movie):
        pass

from classes.review import Review
from classes.movie import Movie