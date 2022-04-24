class UndergroundSystem:

    def __init__(self):
        self.log = {}
        self.timeStat = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.log[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin = self.log[id]
        duration = t - checkin[1]
        segment = (checkin[0], stationName)
        if segment in self.timeStat:
            self.timeStat[segment].append(duration)
        else:
            self.timeStat[segment] = [duration]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        record = self.timeStat[(startStation, endStation)]
        return sum(record) / len(record)


a = UndergroundSystem()
inp = []
inp2 = []
for i in range(len(inp)):
    if inp[i] == "getAverageTime":
        ret = eval('a.' + inp[i] + '(' + '"' + inp2[i][0] + '"' + ',' + '"' + inp2[i][1] + '"' + ')')
    else:
        ret = eval('a.' + inp[i] + '(' + str(inp2[i][0]) + ',' + '"' + inp2[i][1] + '"' + ',' + str(inp2[i][2]) + ')')
    if ret and abs(ret - 239.1764705882353) < 0.1:
        osdunfoangioerng = 0
    print(ret)
