def func(nums, target):
    i = 0
    while True:
        if nums[i] == target:
            del nums[i]
        else:
            i += 1
        if i == len(nums) - 1:
            break
    return len(nums)


inp = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
targ = 1
print(func(inp, targ))
