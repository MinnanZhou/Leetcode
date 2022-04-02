class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        count = 0
        last_error = []
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                count += 1
                if count == 1 and len(last_error) == 0:
                    last_error = [i, j]
                    i += 1
                elif count == 2 and len(last_error) == 2:
                    count -= 1
                    i = last_error[0]
                    j = last_error[1] - 1
                    last_error.pop()
                else:
                    return False
        return True


a = Solution()
inp = "lcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucul"
inp2 = 'abca'
print(a.validPalindrome(inp2))
