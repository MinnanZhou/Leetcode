def func(nums, target):
    i = 0
    k = len(nums) - 1
    j = (k - i) // 2
    if len(nums) == 0:
        return 0
    if target <= nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    while True:
        if nums[j] == target:
            return j
        elif nums[j] > target:
            k = j
            j = round((k + i) / 2 - 0.01)
            m = 1
        else:
            i = j
            j = round((k + i) / 2 + 0.01)
            m = 0
        if k - i <= 1:
            j = j + m
            break
    return j


inp = [1, 3, 5, 6]
val = 5
print(func(inp, val))
