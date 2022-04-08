import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.hp = []
        self.k = k
        for num in nums:
            if len(self.hp) < k:
                heapq.heappush(self.hp, num)
            elif num >= self.hp[0]:
                heapq.heappushpop(self.hp, num)

    def add(self, val: int) -> int:
        if len(self.hp) < self.k:
            heapq.heappush(self.hp, val)
        elif val >= self.hp[0]:
            heapq.heappushpop(self.hp, val)
        return self.hp[0]


a = KthLargest(3, [3, 4, 5, 8])
print(a.add(3))
print(a.add(5))
print(a.add(10))
print(a.add(9))
print(a.add(4))
