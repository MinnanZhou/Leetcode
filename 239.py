import heapq


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        nums.append(nums[-1]-1)
        hp = [[-nums[i], i] for i in range(k)]
        heapq.heapify(hp)
        res = []
        for i in range(k, len(nums)):
            res.append(-hp[0][0])
            while hp and hp[0][1] <= i-k:
                heapq.heappop(hp)
            heapq.heappush(hp, [-nums[i], i])
        return res


a = Solution()
inp = [1]
inp2 = 1
print(a.maxSlidingWindow(inp, inp2))
