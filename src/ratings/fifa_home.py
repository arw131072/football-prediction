from .fifa import FIFASUM

class FIFASUMHome(FIFASUM):
    def __init__(self, home_advantage=100):
        super().__init__()
        self.home_advantage = home_advantage

    def expected_score(self, home_rating, away_rating, neutral):
        if not neutral:
            home_rating += self.home_advantage

        return super().expected_score(
            home_rating,
            away_rating,
            neutral,
        )