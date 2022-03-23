import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        ret = []
        res = []
        heapq.heapify(ret)
        for num2 in nums2:
            for num1 in nums1:
                if len(ret) < k:
                    heapq.heappush(ret, [-num1 - num2, num1, num2])
                elif num1 + num2 < -ret[0][0]:
                    heapq.heappushpop(ret, [-num1 - num2, num1, num2])
                else:
                    break
        for _ in range(k):
            if len(ret) == 0:
                break
            res.append(heapq.heappop(ret)[1:])
        return res[::-1]


a = Solution()
inp1=[]
inp2=[]
k = 10000
print(a.kSmallestPairs(inp1, inp2, k))
