class Subway(object):
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


if __name__ == '__main__':
    subway = Subway()
    subway.checkIn(45, "Leyton", 3)
    subway.checkIn(32, "Paradise", 8)
    subway.checkIn(27, "Leyton", 10)
    subway.checkOut(45, "Waterloo", 15)
    subway.checkOut(27, "Waterloo", 20)
    subway.checkOut(32, "Cambridge", 22)
    print(subway.getAverageTime("Paradise", "Cambridge"))
    print(subway.getAverageTime("Leyton", "Waterloo"))
    subway.checkIn(10, "Leyton", 24)
    print(subway.getAverageTime("Leyton", "Waterloo"))
    subway.checkOut(10, "Waterloo", 38)
    print(subway.getAverageTime("Leyton", "Waterloo"))
