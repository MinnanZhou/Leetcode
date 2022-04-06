class Solution:
    def findWords(self, words):
        dict_set = [set('qwertyuiopQWERTYUIOP'), set('asdfghjklASDFGHJKL'), set('zxcvbnmZXCVBNM')]
        ret = []
        alp, i = None, 0
        for word in words:
            for alp in dict_set:
                if word[0] in alp:
                    break
            for i, letter in enumerate(word):
                if letter not in alp:
                    i -= 1
                    break
            if i == len(word) - 1:
                ret.append(word)
        return ret


a = Solution()
inp = ["abdfs", "cccd", "a", "qwwewm"]
print(a.findWords(inp))
