class Solution:
    def letterCombinations(self, digits: str):
        ret = []
        new = []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        for d in digits:
            if not ret:
                ret = [s for s in mapping[d]]
            else:
                while ret:
                    temp = ret.pop()
                    for newLetter in mapping[d]:
                        new.append(temp + newLetter)
                ret = new.copy()
                new.clear()
        return ret


a = Solution()
inp = '245'
print(a.letterCombinations(inp))
