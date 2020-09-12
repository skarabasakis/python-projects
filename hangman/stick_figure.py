class StickFigure:
    def __init__(self, lives):
        self.__remaining_lives = lives

    def lose_life(self):
        if not self.is_dead():
            self.__remaining_lives -= 1

    def is_dead(self):
        return self.__remaining_lives == 0

    def __str__(self):
        return f"💙 {self.__remaining_lives}"
