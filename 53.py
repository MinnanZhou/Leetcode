def func(nums):
    s = 0
    m = float('-inf')
    for i in range(len(nums)):
        s += nums[i]
        if s > m:
            m = s
        if s < 0:
            s = 0
    return int(m)


inp = [-2,1]
print(func(inp))
