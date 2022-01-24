class Point:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return f'x:{self.x}, y:{self.y}, angle:{self.angle}'