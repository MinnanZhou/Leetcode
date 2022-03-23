class Solution:
    def wiggleSort(self, nums) -> None:
        def top_n(nums, n):
            start = 0
            end = len(nums) - 1
            while True:
                pivot = start
                value = nums[pivot]
                i, j = start, end
                while i < j:
                    while nums[j] >= value and i < j:
                        j -= 1
                    nums[i] = nums[j]
                    while nums[i] < value and i < j:
                        i += 1
                    nums[j] = nums[i]
                nums[i] = value
                if n == i:
                    return
                elif n > i:
                    start = i + 1
                else:
                    end = i - 1

        top_n(nums, len(nums) // 2)
        pos = len(nums[::2])
        if nums[pos-1] == nums[-1]:
            i = -1
            while nums[-1] == nums[i]:
                i -= 1
            nums[-1], nums[i] = nums[i], nums[-1]
        nums[::2], nums[1::2] = nums[:pos][::-1], nums[pos:][::-1]
        return nums


a = Solution()
inp = [0,1,0,6,2,2,2,2]
print(a.wiggleSort(inp))
