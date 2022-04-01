class Solution:
    def reverseString(self, s) -> None:
        for i in range(len(s)): s[i], s[-1 - i] = s[-1 - i], s[i]
