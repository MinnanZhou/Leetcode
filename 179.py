class Solution:
    def largestNumber(self, nums) -> str:
        nums = [str(i) for i in nums]
        nums = self.sort(nums, 0, len(nums) - 1)
        if nums[0] == '0': return '0'
        return ''.join(nums)

    def sort(self, nums, l, r):
        if l > r:
            return []
        if l == r:
            return [nums[l]]
        mid = (l + r) // 2
        return self.merge(self.sort(nums, l, mid), self.sort(nums, mid + 1, r))

    def merge(self, list1, list2):
        res = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] + list2[j] > list2[j] + list1[i]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
        res.extend(list1[i:] or list2[j:])
        return res


a = Solution()
inp = [0, 0]
print(a.largestNumber(inp))
