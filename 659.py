from collections import Counter


class Solution:
    def isPossible(self, nums) -> bool:
        remain = Counter(nums)
        placed = Counter()
        for num in nums:
            if remain[num] == 0:
                continue
            if placed[num - 1] > 0:
                placed[num - 1] -= 1
                placed[num] += 1
                remain[num] -= 1
            elif remain[num + 1] > 0 and remain[num + 2] > 0:
                placed[num + 2] += 1
                remain[num] -= 1
                remain[num + 1] -= 1
                remain[num + 2] -= 1
            else:
                return False
        return True


a = Solution()
inp = [1,2,3,3,4,4,5,5]
print(a.isPossible(inp))
