import bisect


class WordFilter:

    def __init__(self, words):
        self.wordSet = {words[i]: i for i in range(len(words))}
        self.data = sorted(words)

    def f(self, prefix: str, suffix: str) -> int:
        right = bisect.bisect_left(self.data, prefix[:-1] + chr(ord(prefix[-1]) + 1)) - 1
        left = bisect.bisect_left(self.data, prefix)
        l = len(suffix)
        maxIndex = -1
        while right >= left:
            if self.wordSet[self.data[right]] <= maxIndex:
                continue
            m = len(self.data[right])
            if self.data[right][m - l:m] == suffix:
                maxIndex = max(maxIndex, self.wordSet[self.data[right]])
        return maxIndex
