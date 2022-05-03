class Solution:
    def expressiveWords(self, s: str, words) -> int:
        count = 0
        for w in words:
            i, j = 0, 0
            m, n = 0, 0
            l1, l2 = len(w), len(s)
            while True:
                if i >= l1 and j >= l2:
                    count += 1
                    break
                while m < l1 and w[i] == w[m]:
                    m += 1
                while n < l2 and s[j] == s[n]:
                    n += 1
                if w[m - 1] != s[n - 1] or (m - i != n - j and n - j < 3):
                    break
                i, j = m, n
        return count


a = Solution()
inp = "heeellooo"
inp2 = ["hello", "hi", "helo"]
print(a.expressiveWords(inp, inp2))
