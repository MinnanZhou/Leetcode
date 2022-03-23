def func(nums, target):
    if len(nums) < 3:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        else:
            return -1
    if nums[0] < nums[-1]:
        j = 0
        l = 0
        n = len(nums) - 1
    else:
        i = 0
        k = len(nums) - 1
        j = (i + k) // 2
        while True:
            if nums[j] > nums[k]:
                i = j
                j = round((i + k) / 2 + 0.01)
            elif nums[j] < nums[k]:
                k = j
                j = round((i + k) / 2)
            else:
                break
        l = j - len(nums)
        n = j - 1
    m = round((l + n) / 2)
    index = 2
    while True:
        if (2 ** (index - 2)) > len(nums):
            break
        else:
            step = (len(nums) / (2 ** index))
            if int(step) == 0:
                if step > 0:
                    step = 1
            else:
                step = round(step)
        if nums[m] == target:
            return m % len(nums)
        elif nums[m] > target:
            m = m - step
        else:
            m = m + step
        index += 1
    return -1


inp = [1, 2, 3, 5, 6, 7]
tar = 0
print(func(inp, tar))
