# classic calculation of Elo ratings
from .base import RatingSystem

class ClassicElo(RatingSystem):

    def __init__(self):
        super().__init__()
        self.k = 30 # might want to fine tune this based on real data

    def expected_score(
        self,home_rating,
        away_rating,
        neutral,
    ):
        return 1 / ( 1 + 10 ** ((away_rating - home_rating)/ 400))

    def update_factor(self, row):
        return (self.k * self.goal_multiplier(row))