class Solution:
    def longestStrChain(self, words) -> int:
        def check(str1, str2):
            def dp(i, j, used):
                if i == len(str1):
                    return j == len(str2) or (j == len(str2) - 1 and used == 0)
                if used == 2:
                    return False
                if str1[i] != str2[j]:
                    return dp(i, j + 1, used + 1)
                else:
                    return dp(i + 1, j + 1, used) or dp(i, j + 1, used + 1)

            return dp(0, 0, 0)

        words.sort(key=lambda x: -len(x))
        count = [1 for _ in range(len(words))]
        for m in range(len(words)):
            for n in range(m):
                if len(words[m]) == len(words[n]) - 1 and check(words[m], words[n]):
                    count[m] = max(count[m], count[n] + 1)
        return max(count)


a = Solution()
print(a.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
