def func(nums, target):
    nums.sort()
    minimum = float("inf")
    ret = float("inf")
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        for _ in range(len(nums) - 1):
            v = nums[j] + nums[k] + nums[i] - target
            if v == 0:
                return target
            else:
                if minimum > abs(v):
                    minimum = abs(v)
                    ret = nums[j] + nums[k] + nums[i]
                if v > 0:
                    k -= 1
                else:
                    j += 1
            if j == k:
                break
    return int(ret)


inp = [0,1,2]
value = 3
print(func(inp, value))
