def func(nums, target):
    result = [-1, -1]
    if len(nums) < 1:
        return result
    if len(nums) <= 1:
        if nums[0] == target:
            result = [0, 0]
        return result
    if target > nums[-1] or target < nums[0]:
        return result
    i = 0
    k = len(nums) - 1
    j = round((i + k) / 2)
    index = 0
    while True:
        if nums[j] == target:
            break
        elif nums[j] > target:
            k = j
            j = round((i + k) / 2)
        else:
            i = j
            j = round((i + k) / 2 + 0.01)
        index += 1
        if 2 ** (index - 1) > len(nums):
            return result
    start=j
    i = j
    k = len(nums) - 1
    j = round((i + k) / 2)
    while True:
        if nums[j] == nums[i]:
            i = j
            j = round((i + k) / 2 + 0.01)
        else:
            k = j
            j = round((i + k) / 2 - 0.01)
        index += 1
        if j >= len(nums) - 1 and nums[-1] == target:
            break
        if j <= 0 and nums[0] == target:
            break
        if nums[j] == target and nums[j] < nums[j + 1]:
            break
    result[1] = j
    i = 0
    k = start
    j = round((i + k) / 2)
    while True:
        if nums[j] == nums[start]:
            k = j
            j = round((i + k) / 2 - 0.01)
        else:
            i = j
            j = round((i + k) / 2 + 0.01)
        index += 1
        if j >= len(nums) - 1 and nums[-1] == target:
            break
        if j <= 0 and nums[0] == target:
            break
        if nums[j] == target and nums[j] > nums[j - 1]:
            break
    result[0] = j
    return result


inp = [7,8,9]
tar = 8
print(func(inp, tar))
