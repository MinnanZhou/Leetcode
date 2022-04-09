class Solution:
    def findLongestWord(self, s: str, dictionary) -> str:
        dictionary = sorted(dictionary, key=lambda x: [-len(x), x])

        def check(source, target):
            source = iter(source)
            return all(letter in source for letter in target)

        for word in dictionary:
            if check(s, word):
                return word
        return ''


a = Solution()
inp = "abpcplea"
inp2 = ["ale", "apple", "monkey", "plea", "abpcplaaa", "abpcllllll", "abccclllpppeeaaaa"]
print(a.findLongestWord(inp, inp2))
