from collections import Counter
from math import comb


class Solution:
    def threeSumMulti(self, arr, target: int) -> int:
        num_set = set(arr)
        num_count = Counter(arr)
        nums = sorted(list(num_set))
        total = 0
        for index, num in enumerate(nums):
            for num2 in nums[index:]:
                next_t = target - num - num2
                if next_t >= num2 >= num and next_t in num_set:
                    if num == num2 and num2 == next_t and num == next_t:
                        total += comb(num_count[num], 3)
                    elif num == num2:
                        total += num_count[next_t] * comb(num_count[num], 2)
                    elif num == next_t:
                        total += num_count[num2] * comb(num_count[num], 2)
                    elif num2 == next_t:
                        total += num_count[num] * comb(num_count[num2], 2)
                    else:
                        total += num_count[num] * num_count[num2] * num_count[next_t]
        return total%1000000007


a = Solution()
inp=[95,93,46,2,29,41,28,74,9,10]
print(a.threeSumMulti(inp, 196))
