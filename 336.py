class Solution:
    def palindromePairs(self, words):
        ret = []
        dic = {words[index]: index for index in range(len(words))}
        for index, word in enumerate(words):
            lth = len(word)
            if word[::-1] in dic and dic[word[::-1]] != index:
                ret.append((dic[word[::-1]], index))
            for i in range(len(word)):
                prefix = word[:i + 1]
                suffix = word[lth - i - 1:]
                if prefix == prefix[::-1]:
                    if word[i + 1:][::-1] in dic and dic[word[i + 1:][::-1]] != index:
                        ret.append((dic[word[i + 1:][::-1]], index))
                if suffix == suffix[::-1]:
                    if word[:lth - i - 1][::-1] in dic and dic[word[:lth - i - 1][::-1]] != index:
                        ret.append((index, dic[word[:lth - i - 1][::-1]]))

        return list(set(ret))


a = Solution()
inp = ["a", ""]
print(a.palindromePairs(inp))
