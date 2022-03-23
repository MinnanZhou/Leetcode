class Solution:
    def hIndex(self, citations) -> int:
        left = 0
        right = len(citations) - 1
        while left <= right:
            mid = (right + left) // 2
            if citations[mid] >= len(citations) - mid:
                right = mid - 1
            else:
                left = mid + 1
        return len(citations) - left


a = Solution()
inp = [0, 1, 3, 5, 6]
print(a.hIndex(inp))
