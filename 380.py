import random


class RandomizedSet:

    def __init__(self):
        self.data_index = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_index:
            return False
        else:
            self.data.append(val)
            self.data_index[val] = len(self.data) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.data_index:
            pos = self.data_index[val]
            last_value = self.data[-1]
            self.data[pos] = self.data[-1]
            self.data_index[last_value] = pos
            self.data_index.pop(val)
            self.data.pop()
            return True
        return False

    def getRandom(self) -> int:
        pos = random.randint(0, len(self.data) - 1)
        return self.data[pos]


obj = RandomizedSet()
param_1 = obj.insert(0)
param_2 = obj.remove(0)
param_3 = obj.insert(0)
print(param_3)
