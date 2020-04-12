class Accumulator:

    def __init__(self):
        self.count = 0
        self.total = 0

    def add_data_value(self, val):
        self.total += val
        self.count += 1

    def mean(self):
        return self.total / (self.count + 10e-6)

    def __str__(self):
        return "Mean (" + str(self.count) + str(self.total) + "): {:.2f}".format(self.mean())


if __name__ == "__main__":
    Accum = Accumulator()
    print(Accum)
    print("Input value to accumulate!")
    val = input()
    Accum.add_data_value(int(val))
    print("Input value to accumulate!")
    val = input()
    Accum.add_data_value(int(val))
    print(Accum)
