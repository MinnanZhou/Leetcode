from collections import Counter


class Solution:
    def findSubstring(self, s: str, words):
        totalWordLength = len(words) * len(words[0])
        unitLength = len(words[0])
        ret = []
        count = len(words)
        c = Counter(words)
        for i in range(len(s) - totalWordLength + 1):
            counterBoard = dict(c)
            currCount = 0
            for j in range(i, i + totalWordLength + 1, unitLength):
                currStr = s[j:j + unitLength]
                if currStr in counterBoard and counterBoard[currStr] > 0:
                    counterBoard[currStr] -= 1
                    currCount += 1
                else:
                    break
            if currCount == count:
                ret.append(i)

        return ret


a = Solution()
inp = "barfoofoobarthefoobarman"
inp2 = ["bar", "foo", "the"]
print(a.findSubstring(inp, inp2))
