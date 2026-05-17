import constants

class Score:
    def __init__(self):
        """Initialize the score at zero."""
        self.score = 0

    def add_point(self):
        """Increment the score by one."""
        self.score = self.score + 1

    def get_score(self):
        """Return the current score."""
        return self.score
    
    def max_achievable(self):
        """Return the maximum possible score for the current grid and snake length."""
        return constants.TOTAL_CELLS - constants.SNAKE_LENGTH