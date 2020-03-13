from Counter import Counter
import numpy as np

class Flips():

    def __init__(self, n):
        self.n = n

    def main(self):
        heads = Counter("heads")
        tails = Counter("tails")
        for i in range(self.n):
            if np.random.binomial(1, 0.5):
                heads.increment()
            else:
                tails.increment()
        print(heads)
        print(tails)
        delta = abs(heads.tally() - tails.tally())
        print("delta: %d" % delta)

if __name__ == "__main__":
    test_flip = Flips(10)
    test_flip.main()
    test_flip = Flips(10)
    test_flip.main()
    test_flip = Flips(1000000)
    test_flip.main()


