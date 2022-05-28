from collections import Counter


class Solution:
    def isNumber(self, s: str) -> bool:
        c = Counter(s)
        if not s: return False
        if c['e'] + c['E'] > 1 or c['.'] > 1: return False
        if any(letter.isalpha() and letter != 'e' and letter != 'E' for letter in s): return False
        if all(not letter.isdigit() for letter in s): return False

        if c['e']:
            pos = s.index('e')
            return self.isNumber(s[:pos]) and self.isNumber(s[pos + 1:]) == 2
        elif c['E']:
            pos = s.index('E')
            return self.isNumber(s[:pos]) and self.isNumber(s[pos + 1:]) == 2
        else:
            if c['-'] > 1 or c['+'] > 1 or (c['-'] + c['+'] > 1) or (c['-'] > 0 and c['+'] > 0): return False
            if (c['-'] or c['+']) and s[0] not in ['-', '+']: return False
            if c['.'] == 0:
                return 2
            else:
                return True


a = Solution()
l = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "abc",
     "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
# inp="-123.456e789"
for inp in l: print(a.isNumber(inp))
