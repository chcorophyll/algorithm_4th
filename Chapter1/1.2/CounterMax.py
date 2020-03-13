from Counter import Counter
import numpy as np


class CounterMax():

    def __init__(self, n):
        self.n = n

    @staticmethod
    def c_max(x, y):
        if x.tally() > y.tally():
            return x
        else:
            return y

    def main(self):
        heads = Counter("heads")
        tails = Counter("tails")
        for i in range(self.n):
            if np.random.binomial(1, 0.5):
                heads.increment()
            else:
                tails.increment()
        if heads.tally() == tails.tally():
            print("Tie")
        else:
            print(str(self.c_max(heads, tails)) + " wins")


if __name__ == "__main__":
    test_counter = CounterMax(1000000)
    test_counter.main()
