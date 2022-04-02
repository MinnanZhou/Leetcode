class Solution:
    def wordBreak(self, s: str, wordDict):
        wordSet = set(wordDict)
        previous = [False for _ in range(len(s) + 1)]
        previous[0] = True
        comp = [[] for _ in range(len(s) + 1)]
        for i in range(len(s)):
            for j in range(i + 1):
                if previous[j] and s[j:i + 1] in wordSet:
                    comp[j].append(s[j:i + 1])
                    previous[i + 1] = True

        def build(pos):
            if pos >= len(comp) - 1:
                return []
            increment = [[item] for item in comp[pos]]
            sen = []
            for prefix in increment:
                suffix = build(pos + len(prefix[-1]))
                if not suffix and pos + len(prefix[-1]) >= len(comp) - 1: sen.append(prefix)
                for suf in suffix:
                    sen.append(prefix + suf)
            return sen

        if previous[-1]:
            ret = build(0)
            return [' '.join(ret[i]) for i in range(len(ret))]
        return []


a = Solution()
inp = "abcd"
inp2 = ["a","abc","b","cd"]
print(a.wordBreak(inp, inp2))
