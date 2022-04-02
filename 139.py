class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordSet = set(wordDict)
        previous=[True for _ in range(len(s)+1)]
        for i in range(len(s)):
            for j in range(i+1):
                previous[i+1]=previous[j] and s[j:i+1] in wordSet
                if previous[i+1]:
                    break

        return previous[-1]


a = Solution()
inp = "applepenapple"
inp2 = ["apple","pen"]
print(a.wordBreak(inp, inp2))
