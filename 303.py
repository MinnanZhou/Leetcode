class NumArray:

    def __init__(self, nums):
        self.result = [0]
        for num in nums:
            self.result.append(self.result[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.result[right+1] - self.result[left]


a = NumArray([1, 2, 3, 4, 3, 2, 1])
print(a.sumRange(2, 6))
