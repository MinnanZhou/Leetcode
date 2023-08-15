class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = set()
        corr = [''] * 26
        i, j, k = 0, 0, 0
        while i < len(pattern) and j < len(s):
            while j < len(s)-1 and s[j + 1] != ' ':
                j += 1
            current_word = s[k:j + 1]
            if current_word in words:
                if corr[ord(pattern[i]) - 97] != current_word:
                    return False
            elif corr[ord(pattern[i]) - 97] != '':
                return False
            words.add(current_word)
            corr[ord(pattern[i]) - 97] = current_word
            j += 2
            k = j
            i += 1
        return True if i == len(pattern) and j == len(s) + 1 else False


a = Solution()
print(a.wordPattern('abba', "dog cat cat dog"))
