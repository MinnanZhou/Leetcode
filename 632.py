import heapq


class Solution:
    def smallestRange(self, nums):
        hp = [[nums[i][0], i, 0] for i in range(len(nums))]
        heapq.heapify(hp)
        res = [float('-inf'), float('inf')]
        right = max([nums[i][0] for i in range(len(nums))])
        while hp:
            left, i, j = heapq.heappop(hp)
            if right - left < res[1] - res[0]:
                res = [left, right]
            if j == len(nums[i]) - 1:
                return res
            temp = nums[i][j + 1]
            right = max(right, temp)
            heapq.heappush(hp, [temp, i, j + 1])


a = Solution()
inp = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
print(a.smallestRange(inp))
