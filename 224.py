class Solution:
    def calculate(self, s: str) -> int:
        new = ''
        for w in s:
            if w != ' ': new += w
        s = new
        i = 0
        total = 0
        pn = [1]
        while i < len(s):
            if s[i] == '(':
                if i == 0 or s[i - 1] == '+':
                    pn.append(pn[-1])
                else:
                    pn.append(-1 * pn[-1])
                i += 1
            elif s[i] == ')':
                pn.pop()
                i += 1
            else:
                val = ''
                if s[i] not in ['-', '+']:
                    val += '+'
                else:
                    val += s[i]
                    i += 1
                while i < len(s) and s[i].isdigit():
                    val += s[i]
                    i += 1
                total += pn[-1] * int(val) if val not in ['-', '+'] else 0
        return total


a = Solution()
inp = "(1+(4+5+2)-3)+(6+8)"
print(a.calculate(inp))
