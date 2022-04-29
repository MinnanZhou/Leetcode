class Solution:
    def maxChunksToSorted(self, arr) -> int:
        leftMax = [arr[0]]
        for num in arr[1:]:
            currMax = max(leftMax[-1], num)
            while leftMax and num < leftMax[-1]:
                leftMax.pop()
            leftMax.append(currMax)
        return len(leftMax)


a = Solution()
inp = [2, 1, 3, 4, 4]
print(a.maxChunksToSorted(inp))
