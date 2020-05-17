class Interval1D():

    def __init__(self, x, y):
        if x > y:
            print("Exchange Position!")
            self.low = y
            self.high = x
        else:
            self.low = x
            self.high = y

    def __str__(self):
        return "Low: {}, High: {}".format(self.low, self.high)

    def interval_length(self):
        return self.high - self.low

    def interval_contains(self, x):
        if self.low <= x <= self.high:
            return True
        else:
            return False

    def interval_intersect(self, other):
        if self.low > other.high or other.low > self.high:
            return False
        else:
            return True
