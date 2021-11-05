#!/usr/bin/env python
# coding: utf-8
# In[ ]:
# Notice: do not change these function name
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


class subway:
    def __init__(self):
        self.check_in_records = {}
        self.travel_records = {}

    def checkIn(self, cid, station, time):
        self.check_in_records[cid] = CheckInRecord(station, time)

    def checkOut(self, cid, station, time):
        cir = self.check_in_records[cid]
        key = getTravelKey(cir.start_station, station)
        tr = self.travel_records.get(key, TravelRecord())
        tr.addRecord(time - cir.check_in_time)
        self.travel_records[key] = tr

    def getAverageTime(self, start_station, end_station):
        key = getTravelKey(start_station, end_station)
        tr = self.travel_records[key]
        return tr.total_time / tr.count


def getTravelKey(start_station, end_station):
    return "{start},{end}".format(start=start_station, end=end_station)


class CheckInRecord(object):
    def __init__(self, start_station, check_in_time):
        self.start_station = start_station
        self.check_in_time = check_in_time


class TravelRecord(object):
    def __init__(self):
        self.total_time = 0
        self.count = 0

    def addRecord(self, time):
        self.total_time += time
        self.count += 1


class Linear_regression:
    def __init__(self, x, y, m=0, c=0, epochs=200, lr=0.001):
        self.x = x
        self.y = y
        self.m = m
        self.c = c
        self.epochs = epochs
        self.lr = lr

    def gradient_descent(self) -> (float, float):
        def cal_average(li):
            sum_ret = 0
            total_num = 0
            for num in li:
                sum_ret += num
                total_num += 1
            return sum_ret / total_num

        for i in range(self.epochs):
            dm, dc = [], []
            for j in range(len(self.x)):
                yp = self.x[j][0] * self.m + self.c
                dm.append(self.x[j][0] * (yp - self.y[j]))
                dc.append(yp - self.y[j])
            self.m = self.m - self.lr * cal_average(dm)
            self.c = self.c - self.lr * cal_average(dc)
        return self.m, self.c

    def predict(self, x):
        y = []
        for i in range(len(x)):
            y.append(self.m * x[i] + self.c)
        return y


class LCG:
    def __init__(self, seed, multiplier, increment, modulus):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        self.x = seed

    def get_seed(self):
        return self.seed

    def set_seed(self, new_seed):
        self.seed = new_seed

    def initialize(self):
        self.x = self.seed

    def gen(self):
        self.x = (self.multiplier * self.x + self.increment) % self.modulus
        ans = self.x / self.modulus
        return ans

    def seq(self, num):
        seq = []
        for _ in range(num):
            seq.append(self.gen())
        return seq



#
if __name__ == "__main__":
    x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    x_new = [0.9, 0.8, 0.40, 0.7]

    # Test Question 1
    print("\nQ1")
    windowsize = 3
    moving_average = MovingAverage(windowsize)
    step1 = moving_average.next(1)
    print("my answer: ", step1)
    print("right answer: 1.0")
    print("--------------")
    step2 = moving_average.next(10)
    print("my answer: ", step2)
    print("right answer: 5.5")
    print("--------------")
    step3 = moving_average.next(3)
    print("my answer: ", step3)
    print("right answer: 4.66667")
    print("--------------")
    step4 = moving_average.next(5)
    print("my answer: ", step4)
    print("right answer: 6.0")
    print("--------------")

    # Test Question 2
    print("\nQ2")
    s = subway()
    s.checkIn(10, 'Leyton', 3)
    s.checkOut(10, 'Paradise', 8)
    print("my answer: ", s.getAverageTime('Leyton', 'Paradise'))
    print("right answer: 5.0")
    print("--------------")
    s.checkIn(10, 'Leyton', 10)
    s.checkOut(10, 'Paradise', 16)
    print("my answer: ", s.getAverageTime('Leyton', 'Paradise'))
    print("right answer: 5.5")
    print("--------------")
    s.checkIn(10, 'Leyton', 21)
    s.checkOut(10, 'Paradise', 30)
    print("my answer: ", s.getAverageTime('Leyton', 'Paradise'))
    print("right answer: 6.667")
    print("--------------")

    # Test Question 3
    print("\nQ3")
    Linear_model = Linear_regression(x, y, 0, 0, 500, 0.001)
    print("I use m=0, c=0, epochs=500, L=0.001")
    print("my m and c: ", Linear_model.gradient_descent())
    print("right m and c:(35.97890301691016, 46.54235227399102)")
    print("--------------")
    print("my predict: ", Linear_model.predict(x_new))
    print(" right predict: [78.92336498921017, 75.32547468751915,60.93391348075509, 71.72758438582812]")

    # Bonus Question
    print("\nBonus")
    print("set seed = 1, multiplier = 1103515245, increment = 12345, modulus =2 ** 32")
    lcg = LCG(1, 1103515245, 12345, 2 ** 32)
    print("my seed is: ", lcg.get_seed())
    print("right seed is: 1")
    print("the seed is setted with: ", lcg.set_seed(5))
    print("right seed is setted with 5")
    print("the LCG is initialized with seed: ", lcg.initialize())
    print("the LCG is initialized with seed 5")
    print("the next random number is: ", lcg.gen())
    print("right next random number is: 0.2846636981703341")
    print("the first ten sequence is: ", lcg.seq(10))
    print("the first ten sequence is: ", [0.6290451611857861, 0.16200014390051365,
                                          0.4864134492818266, 0.655532845761627, 0.8961918593849987, 0.2762452410534024,
                                          0.8611323081422597, 0.9970241007395089, 0.798466683132574,
                                          0.46138259768486023])