from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        c = Counter()
        ret = ''
        for s in licensePlate:
            if s.isalpha(): c[s.lower()] += 1
        for word in words:
            temp = Counter(word)
            if all(temp[w] >= c[w] for w in temp.keys()) and all(l in temp for l in c.keys()):
                if not ret or len(ret) > len(word):
                    ret = word
        return ret

a=Solution()
inp="Ah71752"
inp2=["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
print(a.shortestCompletingWord(inp,inp2))