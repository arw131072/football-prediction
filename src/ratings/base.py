# all the common logic

from abc import ABC, abstractmethod
from collections import defaultdict
import pandas as pd


class RatingSystem(ABC):

    # set the initial rating for all teams as 1500
    def __init__(self, initial_rating=1500):
        self.initial_rating = initial_rating

    @abstractmethod
    def expected_score(
        self,
        home_rating,
        away_rating,
        neutral,
    ):
        pass

    @abstractmethod
    def update_factor(
        self,
        row,
    ):
        pass

    # matches must be sorted chronologically, otherwise the ratings will be off
    def fit_transform(self, matches):

        ratings = defaultdict(
            lambda: self.initial_rating
        )

        home_ratings = []
        away_ratings = []

        for _, row in matches.iterrows():

            home = row["home_team"]
            away = row["away_team"]

            home_rating = ratings[home]
            away_rating = ratings[away]

            home_ratings.append(home_rating)
            away_ratings.append(away_rating)

            expected_home = self.expected_score(
                home_rating,
                away_rating,
                row["neutral"],
            )

            expected_away = 1 - expected_home

            actual_home, actual_away = (
                self.actual_score(row)
            )

            factor = self.update_factor(row)

            ratings[home] += (factor * (actual_home - expected_home))

            ratings[away] += (factor * (actual_away - expected_away))

        result = matches.copy()

        result["home_rating"] = home_ratings
        result["away_rating"] = away_ratings

        result["rating_diff"] = (result["home_rating"] - result["away_rating"])

        return result

    def actual_score(self, row):

        if pd.notna(row.get("winner")):
            if row["winner"] == row["home_team"]:
                return 0.75, 0.25

            return 0.25, 0.75

        if row["home_score"] > row["away_score"]:
            return 1.0, 0.0

        if row["home_score"] < row["away_score"]:
            return 0.0, 1.0

        return 0.5, 0.5

    # we favor a win of 5-0 more than 1-0, so multiply the update factor by a margin of victory multiplier
    def goal_multiplier(self, row):
        margin = abs(row["home_score"] - row["away_score"])

        if margin <= 1: return 1.0
        if margin == 2: return 1.5

        return (11 + margin) / 8