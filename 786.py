import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr, k: int):
        hp = []
        for i in range(len(arr)):
            for j in range(len(arr) - 1, i, -1):
                frac = arr[i] / arr[j]
                if len(hp) < k:
                    heapq.heappush(hp, (-frac, arr[i], arr[j]))
                elif frac < -hp[0][0]:
                    heapq.heappushpop(hp, (-frac, arr[i], arr[j]))
                else:
                    break
        return hp[0][1:]


a = Solution()
inp = [1, 2, 3, 5, 7, 11]
inp2 = 4
print(a.kthSmallestPrimeFraction(inp, inp2))
