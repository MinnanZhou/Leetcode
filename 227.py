class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join(s.split(' '))
        ops = {'+': 0, '-': 1, '*': 2, '/': 3}

        def add_sub(f):
            count = 0
            i = 0
            num = ''
            last_op = '+'
            while i < len(f):
                if f[i] not in ops:
                    num += f[i]
                    i += 1
                elif f[i] == '+' or f[i] == '-':
                    count = count + float(num) if last_op == '+' else count - int(num)
                    num = ''
                    last_op = f[i]
                    i += 1
                else:
                    j = i
                    while i < len(f) and f[i] != '+' and f[i] != '-':
                        i += 1
                    num = str(mul_div(num + f[j:i]))
            count = count + float(num) if last_op == '+' else count - float(num)
            return count

        def mul_div(f):
            count = 1
            i = 0
            num = ''
            last_op = '*'
            while i < len(f):
                if f[i] not in ops:
                    num += f[i]
                else:
                    count = int(count * float(num) if last_op == '*' else count / float(num))
                    last_op = f[i]
                    num = ''
                i += 1
            count = int(count * float(num) if last_op == '*' else count / float(num))
            return count

        return int(add_sub(s))


a = Solution()
inp = '14/3*2'
print(a.calculate(inp))
