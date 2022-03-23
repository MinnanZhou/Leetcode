def func(nums):
    i = 1
    if len(nums) == 1:
        return
    while True:
        if nums[-i] <= nums[-i - 1]:
            i += 1
            if i == len(nums):
                nums.reverse()
                return
        else:
            break
    nums[-i:] = sorted(nums[-i:])
    index = 0
    for j in nums[-i:]:
        if j > nums[-i - 1]:
            nums[-i - 1], nums[-i + index] = nums[-i + index], nums[-i - 1]
            break
        else:
            index += 1


def getpermutation(nums):
    result = []
    result.append(nums.copy())
    first_permutation = nums.copy()
    while True:
        func(nums)
        if nums == first_permutation:
            break
        result.append(nums.copy())
    return result


inp = [1,3,2]
print(getpermutation(inp))