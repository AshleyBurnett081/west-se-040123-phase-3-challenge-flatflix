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
            raise AttributeError('Not a str between 6 and 16 characters')
    
    
    
    
    
    def reviews(self):
        return[review for review in Review.all if review.viewer is self]
    
    def reviewed_movies(self):
        return [review.movie for review in self.reviews()]

    def has_reviewed_movie(self, movie):
        for review in self.reviews():
            if review.movie == movie:
                return True
            else:
                return False
        

from classes.review import Review
from classes.movie import Movie