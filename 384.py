import random


class Solution:

    def __init__(self, nums):
        self.data = nums
        self.data_ori = nums.copy()

    def reset(self):
        return self.data_ori

    def shuffle(self):
        n = len(self.data)
        for i in range(n - 1, -1, -1):
            j = random.randint(0, i)
            self.data[i], self.data[j] = self.data[j], self.data[i]
        return self.data


a = Solution([1, 2, 3, 4, 5, 6])
print(a.shuffle())
