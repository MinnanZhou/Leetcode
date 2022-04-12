class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        count = 0
        if len(flowerbed) == 1: return False if flowerbed[0] == 1 else n <= 1
        if n == 0: return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
                elif i == len(flowerbed) - 1 and flowerbed[len(flowerbed) - 2] == 0:
                    flowerbed[i] = 1
                    count += 1
                elif flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1]:
                    flowerbed[i] = 1
                    count += 1
        return count >= n


a = Solution()
inp = [1, 0, 1, 0, 1]
print(a.canPlaceFlowers(inp, 2))
