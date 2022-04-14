class Solution:
    def findLongestChain(self, pairs) -> int:
        pairs.sort()
        count, last = 0, float('-inf')
        for i, p in enumerate(pairs):
            if p[0] > last:
                count += 1
                last = p[1]
            elif p[1] < last:
                last = p[1]

        return count


a = Solution()
inp = [[1, 2], [2, 3], [3, 4], [4, 5], [7, 8]]
print(a.findLongestChain(inp))
