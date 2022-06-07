class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''
        for l in s:
            if l.isalpha() or l.isdigit():
                c += l.lower()
        return c == c[::-1]
