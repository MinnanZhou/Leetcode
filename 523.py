class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        rem = []
        past = set()
        past.add(0)
        for i, num in enumerate(nums):
            if num % k != 0:
                rem.append(num % k)
            elif i < len(nums) and nums[i + 1] % k == 0:
                return True
        last_rem = 0
        for r in rem:
            last_rem = (last_rem + r) % k
            if last_rem in past:
                return True
            past.add(last_rem)
        return False


a = Solution()
inp = [23, 2, 4, 6, 6]
inp2 = 7
print(a.checkSubarraySum(inp, inp2))
