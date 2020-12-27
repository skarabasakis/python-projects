class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def quarter():
        return "quarter"

    def in_quarter(self, quarter):
        if (quarter == 1):
            return self.x > 0 and self.y > 0
        if (quarter == 2):
            return self.x < 0 and self.y > 0
        if (quarter == 3):
            return self.x < 0 and self.y < 0
        if (quarter == 4):
            return self.x > 0 and self.y < 0
