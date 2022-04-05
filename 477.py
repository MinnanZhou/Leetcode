class Solution:
    def totalHammingDistance(self, nums) -> int:
        mask = 1
        dis = 0
        for _ in range(32):
            count_zero, count_one = 0, 0
            for num in nums:
                if num & mask:
                    count_one += 1
                else:
                    count_zero += 1
            dis += count_one * count_zero
            mask = mask << 1
        return dis


a = Solution()
inp = [4, 14, 4]
print(a.totalHammingDistance(inp))
