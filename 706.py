class MyHashMap:

    def __init__(self):
        self.hashset = [[] for _ in range(1001)]

    def put(self, key: int, value: int) -> None:
        pos = key % 1001
        for index, item in enumerate(self.hashset[pos]):
            if item[0] == key:
                self.hashset[pos][index] = (key, value)
                return
        self.hashset[pos].append((key, value))

    def get(self, key: int) -> int:
        pos = key % 1001
        for item in self.hashset[pos]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        pos = key % 1001
        for index, item in enumerate(self.hashset[pos]):
            if item[0] == key:
                self.hashset[pos][index], self.hashset[pos][-1] = self.hashset[pos][-1], self.hashset[pos][index]
                self.hashset[pos].pop()
                return


a=MyHashMap()
a.put(2,1)
a.put(2,1)
a.get(2)
a.remove(2)
a.get(2)