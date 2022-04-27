import bisect


class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        x = bisect.bisect_right(letters, target)
        return letters[x if x != len(letters) else 0]
