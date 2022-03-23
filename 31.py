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


func([5, 1, 1])
