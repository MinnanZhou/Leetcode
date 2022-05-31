class Solution:
    def restoreIpAddresses(self, s: str):
        if len(s) > 12 or len(s) < 4:
            return []
        ret = set()

        def divide(count, path, string):
            if count == 4 and len(string) == 0:
                ret.add(path[1:])
            elif count == 4 or len(string) == 0:
                return
            else:
                divide(count + 1, path + '.' + string[:1], string[1:])
                if string[0] == '0' or len(string) == 1: return
                divide(count + 1, path + '.' + string[:2], string[2:])
                if len(string) == 2: return
                if int(string[:3]) <= 255:
                    divide(count + 1, path + '.' + string[:3], string[3:])
                return

        divide(0, '', s)
        return ret


a = Solution()
inp = "101023"
print(a.restoreIpAddresses(inp))
