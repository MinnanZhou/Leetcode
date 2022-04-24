class MyHashSet:

    def __init__(self):
        self.hashset = [[] for _ in range(1001)]

    def add(self, key: int) -> None:
        pos = ((key * 1000009) % 1000000007) % 1001
        if key not in self.hashset[pos]:
            self.hashset[pos].append(key)

    def remove(self, key: int) -> None:
        pos = ((key * 1000009) % 1000000007) % 1001
        if key in self.hashset[pos]: self.hashset[pos].remove(pos)

    def contains(self, key: int) -> bool:
        pos = ((key * 1000009) % 1000000007) % 1001
        return key in self.hashset[pos]
