from Counter import Counter
import numpy as np


class Rolls():

    def __init__(self, roll=None):
        self.sides = 6
        if not roll:
            self.roll = [Counter(str(i+1) + "'s") for i in range(self.sides)]

    def main(self, num):
        for i in range(num):
            result = np.random.randint(0, self.sides)
            self.roll[result].increment()
        for roll in self.roll:
            print(roll)


if __name__ == "__main__":
    rolls = Rolls()
    rolls.main(1000000)
