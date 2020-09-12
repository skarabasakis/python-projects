class Puzzle:
    def __init__(self, solution):
        self.__solution = solution.upper()
        self.__revealed = [(False if c.isalpha() else True) for c in solution]

    def __str__(self):
        return ''.join([(l if self.__revealed[i] else '_') for i, l in enumerate(list(self.__solution))])

    def guess(self, letter):
        letter = letter.upper()
        letter_positions = [i for i, c in enumerate(list(self.__solution)) if letter == c]

        for position in letter_positions:
            self.__revealed[position] = True

        return bool(letter_positions)

    def is_revealed(self):
        """ Check if all puzzle letters have been revealed """
        return all(self.__revealed)

    def reveal(self):
        """ Force all puzzle letters to be revealed """
        self.__revealed = [True for c in list(self.__solution)]
