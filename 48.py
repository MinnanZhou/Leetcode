def rotate(nums):
    for i in nums:
        i.reverse()
    for i in range(len(inp)):
        for j in range(len(inp)-i):
            nums[i][j], nums[len(inp) - j - 1][len(inp) - i - 1] = nums[len(inp) - j - 1][len(inp) - i - 1], nums[i][j]
    return nums


inp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(inp))
