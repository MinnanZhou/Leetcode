class Solution:
    def maxChunksToSorted(self, arr) -> int:
        leftMax = float('-inf')
        count = 0
        for i, a in enumerate(arr):
            leftMax = max(leftMax, a)
            if leftMax == i: count += 1
        return count
