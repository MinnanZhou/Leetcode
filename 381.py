import random


class RandomizedCollection:

    def __init__(self):
        self.data_index = {}
        self.data = []

    def insert(self, val: int) -> bool:
        self.data.append(val)
        if val in self.data_index and self.data_index[val]:
            self.data_index[val].add(len(self.data) - 1)
            return False
        else:
            self.data_index[val] = {len(self.data) - 1}
            return True

    def remove(self, val: int) -> bool:
        if self.data_index[val]:
            pos = self.data_index[val].pop()
            if pos != len(self.data) - 1:
                last_value = self.data[-1]
                self.data[pos] = self.data[-1]
                self.data_index[last_value].add(pos)
                self.data_index[last_value].remove(len(self.data)-1)
            self.data.pop()
            return True
        return False

    def getRandom(self) -> int:
        pos = random.randint(0, len(self.data) - 1)
        return self.data[pos]


obj = RandomizedCollection()
param = [0] * 15
param[1] = obj.insert(0)
param[2] = obj.remove(0)
param[3] = obj.insert(0)
param[4] = obj.insert(0)
param[5] = obj.insert(0)
param[6] = obj.insert(1)
param[7] = obj.insert(2)
param[8] = obj.insert(1)
param[9] = obj.remove(0)
param[10] = obj.remove(1)
param[11] = obj.remove(1)
param[12] = obj.remove(0)
param[13] = obj.remove(0)
param[14] = obj.remove(0)
print(param)
