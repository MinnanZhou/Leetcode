class Solution:
    def fullJustify(self, words, maxWidth):
        total_len = 0
        ret = []
        line = ''
        group = []
        amount = 0
        for i in range(len(words)):
            if total_len == 0:
                total_len += len(words[i])
                group.append(words[i])
                amount += 1
            elif total_len + len(words[i]) + 1 <= maxWidth:
                total_len += len(words[i]) + 1
                group.append(words[i])
                amount += 1
            else:
                spaces = maxWidth - total_len + amount - 1
                if amount == 1:
                    line += group[0] + ' ' * spaces
                else:
                    avg = spaces // (amount - 1)
                    exc = spaces % (amount - 1)
                    for j in range(amount - 1):
                        if exc > 0:
                            line += group[j] + ' ' * (avg + 1)
                            exc -= 1
                        else:
                            line += group[j] + ' ' * avg
                    line += group[-1]
                ret.append(line)
                line = ''
                group = [words[i]]
                total_len = len(words[i])
                amount = 1
            if i == len(words) - 1:
                spaces = maxWidth - total_len
                if amount == 1:
                    group[0] += ' ' * (maxWidth - len(words[i]))
                    ret.append(group[0])
                else:
                    for j in range(amount - 1):
                        line += group[j] + ' '
                    line += group[-1] + ' '*spaces
                    ret.append(line)
        return ret


a = Solution()
inp = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
print(a.fullJustify(inp, 20))
