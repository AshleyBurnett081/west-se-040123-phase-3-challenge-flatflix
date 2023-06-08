class Movie:
    all = []
    
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)
    
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 1 <= len(title):
            self._title = title
        else:
            raise AttributeError('Not from title class')
    
    
    def reviews(self):
        return [review for review in Review.all if review.movie is self]
    
    def reviewers(self):
        return list({review.viewer for review in self.reviews()})
    
    def average_rating(self):
        rating = [review.rating for review in self.reviews()]
        return mean(rating) if rating else 'No rating yet'
    
    @classmethod
    def highest_rated(cls):
        return max(cls.all, key = lambda rating : rating.average_rating())
    
from classes.review import Review
from classes.viewer import Viewer
from statistics import mean
