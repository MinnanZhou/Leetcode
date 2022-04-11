class Solution:
    def calPoints(self, ops) -> int:
        ret = []
        for op in ops:
            if op == 'C':
                ret.pop()
            elif op == 'D':
                ret.append(int(ret[-1]) * 2)
            elif op == '+':
                ret.append(int(ret[-1]) + int(ret[-2]))
            else:
                ret.append(int(op))
        return sum(ret)
