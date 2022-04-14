import bisect
from collections import deque


class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        arr = [float('-inf')] + arr + [float('inf')]
        start = bisect.bisect_left(arr, x)
        if arr[start] == x:
            ret = deque([x])
            l, r = start - 1, start + 1
            k -= 1
        else:
            ret = deque()
            l, r = start - 1, start
        while k > 0:
            if x - arr[l] <= arr[r] - x:
                ret.appendleft(int(arr[l]))
                l -= 1
            else:
                ret.append(int(arr[r]))
                r += 1
            k -= 1
        return ret
