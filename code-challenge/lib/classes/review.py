class Review:
    all =[]
    
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        type(self).all.append(self)
        
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise AttributeError('Not from Viewer class')
        
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise AttributeError('Not from Movie class')
        
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and rating in range (1,6):
            self._rating = rating
        else:
            raise AttributeError('Not from rating class')
    
    











from classes.movie import Movie
from classes.viewer import Viewer