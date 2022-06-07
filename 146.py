from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.pairs = OrderedDict()
        self.maxAmount = capacity

    def get(self, key: int) -> int:
        if key not in self.pairs:
            return -1
        self.pairs.move_to_end(key)
        return self.pairs[key]

    def put(self, key: int, value: int) -> None:
        if key in self.pairs:
            self.pairs[key] = value
            self.pairs.move_to_end(key)
        else:
            if len(self.pairs) == self.maxAmount:
                self.pairs.popitem(last=False)
            self.pairs[key] = value
