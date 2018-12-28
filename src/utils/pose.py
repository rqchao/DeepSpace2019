class Pose:
    """A simple class to store position (x and y values),
    and orientation (angle)."""

    def __init__(self, x=0.0, y=0.0, angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.angle == other.angle)

    def __str__(self):
        return "({}, {}, {})".format(round(self.x, 3), round(self.y, 3), round(self.angle, 3))
