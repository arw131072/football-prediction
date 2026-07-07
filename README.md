# Football Prediction

Predict FIFA World Cup group-stage outcomes using:

- Elo ratings
- Multinomial logistic regression
- Poisson score models
- Monte Carlo simulations

This is an unofficial simulator and is not affiliated with FIFA. The methodology for calculating ELO rankings is inspired by the FIFA SUM method.

**Packages:**

`RatingSystem.py` is responsible for:

- Maintaining team ratings.
- Iterating through matches chronologically.
- Recording pre-match ratings as features
- Updating ratings after each match.
- Delegating the model-specific pieces to subclasses:
  - expected_score()
  - update_factor()

