class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        def check(i, j, k):
            if k == len(s3):
                return True
            if i < len(s1) and j < len(s2) and s3[k] == s1[i] == s2[j]:
                return check(i + 1, j, k + 1) or check(i, j + 1, k + 1)
            elif i < len(s1) and s3[k] == s1[i]:
                return check(i + 1, j, k + 1)
            elif j < len(s2) and s3[k] == s2[j]:
                return check(i, j + 1, k + 1)
            return False

        return check(0, 0, 0)


a = Solution()
inp = "aabcc"
inp2 = "dbbca"
inp3 = "aadbbcbcac"
print(a.isInterleave(inp, inp2, inp3))
