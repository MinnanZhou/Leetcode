class Solution:
    def findLength(self, nums1, nums2) -> int:
        p, x = 1000000007, 113
        hashList1 = [0 for _ in range(len(nums1) + 1)]
        hashList2 = [0 for _ in range(len(nums2) + 1)]
        for i in range(len(nums1)):
            hashList1[i + 1] = (hashList1[i] * x + nums1[i]) % p
        for j in range(len(nums2)):
            hashList2[j + 1] = (hashList2[j] * x + nums2[j]) % p

        def getHash(hashList, left, right):
            return ((hashList[right] - hashList[left] * x ** (right - left)) + p) % p

        start, end, ans = 1, min(len(nums1), len(nums2)), 0
        while start <= end:
            mid = (start + end) // 2
            sub = set()
            exist = 0
            for i in range(len(nums1) - mid + 1):
                sub.add(getHash(hashList1, i, i + mid))
            for j in range(len(nums2) - mid + 1):
                if getHash(hashList2, j, j + mid) in sub:
                    start = mid + 1
                    ans = mid
                    exist = 1
                    break
            if not exist: end = mid - 1
        return ans

    def ch(self, array):
        x = 113
        p = 1000000007
        h = 0
        for num in array:
            h = h * x + num
        return h % p


a = Solution()
inp = [1, 2, 3, 2, 1, 0]
inp2 = [3, 2, 1, 0, 4, 7]
print(a.findLength(inp, inp2))
