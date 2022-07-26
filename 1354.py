import heapq


class Solution:
    def isPossible(self, target) -> bool:
        target = [-i for i in target]
        heapq.heapify(target)
        s = -sum(target)
        while target:
            if target[0] == -1:
                return True
            diff = s - (-target[0])
            if -target[0] <= diff or diff == 0:
                return False
            rem = ((-target[0]) - 1) % diff + 1
            s = s - (-target[0]) + rem
            heapq.heappushpop(target, -rem)


a = Solution()
inp = [8, 5]
print(a.isPossible(inp))
