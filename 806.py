class Solution:
    def numberOfLines(self, widths, s: str):
        currLen = 100
        lines = 1
        for letter in s:
            if currLen < widths[ord(letter) - 97]:
                currLen = 100
                lines += 1
            else:
                currLen -= widths[ord(letter) - 97]
        return [lines, currLen]
