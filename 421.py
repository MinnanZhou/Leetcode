class Solution:
    def findMaximumXOR(self, nums) -> int:
        ans = 0
        for i in range(32)[::-1]:
            ans = ans << 1
            prefix = set([num >> i for num in nums])
            ans_candidate = ans + 1
            for p in prefix:
                if p ^ ans_candidate in prefix:
                    ans = ans_candidate
                    break
        return ans


a = Solution()
inp = [3, 10, 5, 25, 2, 8]
print(a.findMaximumXOR(inp))
