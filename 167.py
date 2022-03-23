class Solution:
    def twoSum(self, numbers, target: int):
        left = 0
        right = len(numbers) - 1
        for _ in range(len(numbers)):
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1


a = Solution()
inp = [1, 2, 3, 5, 6]
print(a.twoSum(inp, 11))
