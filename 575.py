class Solution:
    def distributeCandies(self, candyType) -> int:
        return min(len(candyType)//2, len(set(candyType)))