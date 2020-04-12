import functools
import math


@functools.total_ordering
class Point2D():

    def __init__(self, x=None, y=None, r=None, a=None):
        self._x = 0.0
        self._y = 0.0
        self._r = 0.0
        self._a = 0.0
        if type(x) == Point2D:
            self._x = x.x
            self._y = x.y
            self._r = x.r
            self._a = x.a
        elif type(x) == tuple:
            self._x = x[0]
            self._y = x[1]
            self._r = math.sqrt(x[0]**2 + x[1]**2)
            self._a = math.atan2(x[1], x[0])
        elif (not x == None) and (not y == None):
            self._x = x
            self._y = y
            self._r = math.sqrt(x**2 + y**2)
            self._s = math.atan2(y, x)
        elif (not r == None) and (not a == None):
            self._r = r
            self._a = a
            self._x = r * math.cos(a)
            self._y = r * math.sin(a)

    def _calc_cartesian(self):
        self._x = self._r * math.cos(self._a)
        self._y = self._e * math.sin(self._a)

    def _calc_polar(self):
        self._r = math.sqrt(self._x**2 + self._y**2)
        self._a = math.atan2(self._y, self._x)

    def cartesian(self, x=None, y=None):
        if not x:
            return (self._x, self._y)
        elif type(x) == tuple:
            self._x = float(x[0])
            self._y = float(x[1])
            self._calc_polar()
        elif not x == None and not y == None:
            self._x = float(x)
            self._y = float(y)
            self._calc_polar()

    def polar(self, r=None, a=None):
        if not r:
            return (self._r, self._a)
        elif type(r) == tuple:
            self._r = float(r[0])
            self._a = float(r[1])
            self._calc_cartesian()
        elif not r == None and not a == None:
            self._r = r
            self._a = a
            self._calc_cartesian()

    def ints(self):
        return (int(self._x), int(self._y))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val
        self._calc_polar()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val
        self._calc_polar()

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, val):
        self._r = val
        self._calc_cartesian()

    @property
    def a(self):
        return  self._a

    @a.setter
    def a(self, val):
        self._a = val
        self._calc_cartesian()

    def __repr__(self):
        return "Point2D({}, {})({}, {})".format(self._x, self._y, self._r, self._a)

    def __add__(self, other):
        return Point2D(self._x + other.x, self._y + other.y)

    def __iadd__(self, other):
        self._x += other.x
        self._y += other.y
        self._calc_polar()
        return self

    def __sub__(self, other):
        return Point2D(self._x - other.x, self._y - other.y)

    def __isub__(self, other):
        self._x -= other.x
        self._y -= other.y
        self._calc_polar()
        return self

    def __mul__(self, val):
        return Point2D(r=self.r*val, a=self.a)

    def __rmul__(self, val):
        return Point2D(r=self.r*val, a=self.a)

    def __imul__(self, val):
        self.r *= val
        return self

    def __lt__(self, other):
        if self._x == other._x:
            return self._y < other._y
        return self._x < other._x

    def __eq__(self, other):
        return (self._x == other._x) and (self._y and other._y)

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

