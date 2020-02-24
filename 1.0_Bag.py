from utils.linklist import Node, LinkIterator


class Bag:

    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(str(i) for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def add(self, item):
        old_first = self.first
        self.first = Node(item, old_first)
        self.n += 1


if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        bag = Bag()
        for item in line.split():
            bag.add()