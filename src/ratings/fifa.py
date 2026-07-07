from .base import RatingSystem
from src.utils.tournament import tournament_importance


class FIFASUM(RatingSystem):

    def expected_score(
        self,
        home_rating,
        away_rating,
        neutral,
    ):
        dr = home_rating - away_rating
        return 1 / (1 + 10 ** (-dr / 600)) 
        # uses 600 to flatten the curve: stronger team is expected to win, but not by as much

    # dynamic K factor based on tournament importance and goal difference
    def update_factor(self, row):
        importance = tournament_importance(row["tournament"])
        return importance * self.goal_multiplier(row)