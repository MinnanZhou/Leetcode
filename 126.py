from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        used = {}
        wordSet = set(wordList)
        ret = []
        used[beginWord] = [[beginWord]]

        while used:
            new = defaultdict(list)
            for k in used.keys():
                if k == endWord:
                    ret+=used[k]
                for i in range(len(k)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        x = k[:i] + j + k[i + 1:]
                        if x in wordSet:
                            new[x] += [m + [x] for m in used[k]]
            wordSet -= new.keys()
            used = new
        return ret


a = Solution()
inp = "red"
inp2 = "tax"
inp3 = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
print(a.findLadders(inp, inp2, inp3))
