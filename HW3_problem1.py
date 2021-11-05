class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.sum = 0
        self.con = []

    def next(self, val):
        if len(self.con) == self.size:
            self.sum -= self.con[0]
            self.con = self.con[1:]
        self.con.append(val)
        self.sum += val
        return self.sum / len(self.con)


if __name__ == '__main__':
    ma = MovingAverage(3)
    print(ma.next(1))
    print(ma.next(10))
    print(ma.next(3))
    print(ma.next(5))
