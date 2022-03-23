class Solution:
    def rotate(self, nums, k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums.pop())


a = Solution()
inp = [1, 2, 3, 4, 5, 6, 7]
inp2 = 3
a.rotate(inp, inp2)
