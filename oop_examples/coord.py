class Coord:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other = None):
        other = other or Coord(0, 0)
        return ((self.x - other.x )**2 + (self.y-other.y)**2)**0.5

    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return 1
        if self.x < 0 and self.y > 0:
            return 2
        if self.x < 0 and self.y < 0:
            return 3
        if self.x > 0 and self.y < 0:
            return 4
