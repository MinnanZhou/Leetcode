class Solution:
    def generateParenthesis(self, n: int):
        ret = [set() for _ in range(n)]
        ret[0].add('()')
        for k in range(1, n):
            while ret[k-1]:
                temp = ret[k-1].pop()
                for i in range(len(temp)):
                    for j in range(i, len(temp)):
                        ret[k].add(temp[:i] + '(' + temp[i:j] + ')' + temp[j:])
        return list(ret[-1])


a = Solution()
print(a.generateParenthesis(5))
