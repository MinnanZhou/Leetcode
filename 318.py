class Solution:
    def maxProduct(self, words) -> int:
        dict_array = []
        ret = 0
        for word in words:
            x = set()
            for letter in word:
                x.add(letter)
            dict_array.append(x)
        for i in range(len(dict_array)):
            for k in range(i + 1, len(dict_array)):
                co = dict_array[i].copy()
                for j in range(len(dict_array[i])):
                    x = co.pop()
                    if x in dict_array[k]:
                        break
                    elif j == len(dict_array[i])-1:
                        ret = max(ret, len(words[i]) * len(words[k]))
        return ret


a = Solution()
print(a.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
