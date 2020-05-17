from Interval1D import Interval1D
from Point2D import Point2D


class Interval2D():

    def __init__(self, x, y):
        assert isinstance(x, Interval1D)
        assert isinstance(y, Interval1D)
        self.axis_x = x
        self.axis_y = y
        self.point_low = Point2D(self.axis_x.low, self.axis_y.low)
        self.point_high = Point2D(self.axis_x.high, self.axis_y.high)

    def __str__(self):
        return "Axis X: {}, Axis Y: {}".format(self.axis_x, self.axis_y)

    def interval_area(self):
        axis_x_length = self.axis_x.high - self.axis_x.low
        axis_y_length = self.axis_y.high - self.axis_y.low
        return axis_x_length * axis_y_length

    def interval_contains(self, p):
        assert isinstance(p, Point2D)
        if self.axis_x.low <= p.x <= self.axis_x.high and self.axis_y.low <= p.y <= self.axis_y.high:
            return True
        else:
            return False

    def interval_intersect2d(self, other):
        assert isinstance(other, Interval2D)
        if self.axis_x.interval_intersect(other.axis_x) or self.axis_y.interval_intersect(other.axis_y):
            return True
        else:
            return False
