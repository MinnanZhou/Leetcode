import bisect


class Solution:
    def findNumberOfLIS(self, nums) -> int:
        if not nums: return 0
        n = len(nums)
        length = [{} for _ in range(n + 1)]
        length[0] = {float('-inf'): 1}
        length[1] = {nums[0]: 1}
        minRecord = [float('inf') for _ in range(n + 1)]
        minRecord[1] = nums[0]
        minRecord[0] = float('-inf')
        recordList = [[] for _ in range(n + 1)]
        recordList[1].append(nums[0])
        recordList[0].append(float('-inf'))
        for i in range(1, len(nums)):
            pos1 = bisect.bisect_left(minRecord, nums[i]) - 1
            pos2 = bisect.bisect_left(recordList[pos1], nums[i])
            total = sum([length[pos1][recordList[pos1][j]] for j in range(pos2)])
            if nums[i] in length[pos1 + 1]:
                length[pos1 + 1][nums[i]] += total
            else:
                length[pos1 + 1][nums[i]] = total
                bisect.insort_left(recordList[pos1 + 1], nums[i])
            minRecord[pos1 + 1] = min(minRecord[pos1 + 1], nums[i])

        k = -1
        while not length[k]: k -= 1
        return sum(length[k].values())


a = Solution()
inp = [2,2,2,2]
print(a.findNumberOfLIS(inp))
