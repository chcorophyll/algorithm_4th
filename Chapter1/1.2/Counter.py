class Counter():

    def __init__(self, name):
        self.count = 0
        self.name = name

    def increment(self):
        self.count += 1

    def tally(self):
        return self.count

    def __str__(self):
        return str(self.count) + self.name


if __name__ == "__main__":
    heads = Counter("heads")
    tails = Counter("tails")

    heads.increment()
    heads.increment()
    tails.increment()

    print(heads)
    print(tails)
