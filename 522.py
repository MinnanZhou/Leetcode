class Solution:
    def findLUSlength(self, strs) -> int:
        strs = sorted(strs, key=lambda x: -len(x))

        def check(target, compare):
            return all(t in compare for t in target)

        for i, word in enumerate(strs):
            if all(not check(word, strs[j]) for j in range(len(strs)) if j != i):
                return len(word)
        return -1


a=Solution()
print(a.findLUSlength(["aabbcc", "aabbcc","c"]))