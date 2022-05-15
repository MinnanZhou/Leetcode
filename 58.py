class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        count = 1
        while s[i] != ' ':
            count += 1
            i -= 1
        return count
