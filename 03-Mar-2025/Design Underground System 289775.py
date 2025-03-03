# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:
    def __init__(self):
        self.travel_time = {}
        self.checkins = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, checkin_time = self.checkins.pop(id)
        travel = (start, stationName)
        travel_time = t - checkin_time

        if travel in self.travel_time:
            tot, count = self.travel_time[travel]
            self.travel_time[travel] = (tot + travel_time, count + 1)
        else:
            self.travel_time[travel] = (travel_time, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation)
        total_time, count = self.travel_time[travel]
        return total_time / count
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)