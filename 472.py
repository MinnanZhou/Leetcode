class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        wordSet = set(words)

        def check(s):
            previous = [False for _ in range(len(s) + 1)]
            previous[0] = True
            for i in range(len(s)):
                for j in range(i + 1):
                    if previous[j] and s[j:i + 1] in wordSet:
                        previous[i + 1] = True
            return previous[-1]

        ret = []
        for word in words:
            if len(word)<1:
                continue
            wordSet.remove(word)
            if check(word):
                ret.append(word)
            wordSet.add(word)
        return ret


a = Solution()
inp = [""]
print(a.findAllConcatenatedWordsInADict(inp))
