def func(nums):
    i = 0
    while True:
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
        if i == len(nums) - 1:
            break
    return len(nums), nums


inp = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
x,y=func(inp)
pass