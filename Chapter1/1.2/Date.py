from functools import total_ordering

@total_ordering
class Date_Java():

    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return "{}-{}-{}".format(instance.__dict__[self.month],
                                     instance.__dict__[self.day],
                                     instance.__dict__[self.year]
                                     )

    def __set__(self, instance, month, day, year):
        if not isinstance(month, int):
            raise TypeError("Expect an int")
        if not isinstance(day, int):
            raise TypeError("Expect an int")
        if not isinstance(year, int):
            raise TypeError("Expect an int")
        if not month in range(1, 13):
            raise TypeError("Expected int in 1-12")
        if not day in range(1, 32):
            raise TypeError("Expected int in 1-12")
        instance.__dict__[self.month] = month
        instance.__dict__[self.day] = day
        instance.__dict__[self.year] = year

    def __del__(self, instance):
        del instance.__dict__[self.month]
        del instance.__dict__[self.day]
        del instance.__dict__[self.year]

    def __str__(self):
        return "Date: {}_{}_{}".format(self.month, self.day, self.year)

    def __eq__(self, other):
        return (self.month, self.day, self.year) == (other.month, other.day, other.year)

    def __hash__(self):
        return hash("{}-{}-{}".format(self.month, self.day, self.year))
