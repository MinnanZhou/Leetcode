class Solution:
    def minimumLengthEncoding(self, words) -> int:
        words.sort(key=lambda x: -len(x))
        wordsSet = set(words)
        count = 0
        for word in words:
            if word in wordsSet:
                for i in range(len(word) - 1, -1, -1):
                    if word[i:] in wordsSet:
                        wordsSet.remove(word[i:])
                count += len(word) + 1
        return count


a = Solution()
inp = ["t"]
print(a.minimumLengthEncoding(inp))
