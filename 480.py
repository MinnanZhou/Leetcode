import bisect


class Solution:
    def medianSlidingWindow(self, nums, k: int):
        ret = []
        window = nums[:k]
        window.sort()
        if k % 2 == 0:
            ret.append((window[k // 2] + window[k // 2 - 1]) / 2)
        else:
            ret.append(window[k // 2])
        for i in range(k, len(nums)):
            window.remove(nums[i - k])
            bisect.insort_left(window, nums[i])
            if k % 2 == 0:
                ret.append((window[k // 2] + window[k // 2 - 1]) / 2)
            else:
                ret.append(window[k // 2])
        return ret


a = Solution()
inp = [1, 3, -1, -3, 5, 3, 6, 7]
print(a.medianSlidingWindow(inp, k=3))
