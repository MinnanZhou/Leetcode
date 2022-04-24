import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        ret = []
        res = []
        visited = set()
        heapq.heappush(ret, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))
        while len(res) < k and ret:
            val, x, y = heapq.heappop(ret)
            res.append((nums1[x], nums2[y]))
            if x + 1 < len(nums1) and (x + 1, y) not in visited:
                heapq.heappush(ret, (nums1[x + 1] + nums2[y], x + 1, y))
                visited.add((x + 1, y))
            if y + 1 < len(nums2) and (x, y + 1) not in visited:
                heapq.heappush(ret, (nums1[x] + nums2[y + 1], x, y + 1))
                visited.add((x, y + 1))
        return res


a = Solution()
inp1 = [1, 1, 2]
inp2 = [1, 2, 3]
k = 10
print(a.kSmallestPairs(inp1, inp2, k))
