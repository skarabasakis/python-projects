from puzzle import Puzzle
from stick_figure import StickFigure


class Hangman:
    """Example usage: Hangman("hello world") """

    def __init__(self, solution, lives=7):
        self.__puzzle = Puzzle(solution)
        self.__stick_figure = StickFigure(lives)

    def __str__(self):
        return f"{self.__stick_figure} | {self.__puzzle}"

    def __play_round(self):
        if not self.__puzzle.guess(input('Guess a letter: ')):
            self.__stick_figure.lose_life()

    def __result(self):
        if self.__stick_figure.is_dead():
            return "💀 YOU LOST"
        else:
            return "🏆 YOU WON"

    def play(self):
        while not self.__puzzle.is_revealed():
            print(self)
            self.__play_round()
            if self.__stick_figure.is_dead():
                self.__puzzle.reveal()

        print(self)
        print(self.__result())


if __name__ == "__main__":
    Hangman("hello world").play()
