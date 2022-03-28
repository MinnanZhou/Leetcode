def func(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    i = 0
    j = i + 1
    k = j + 1
    result = []
    result2 = []
    while True:
        current = nums[i] + nums[j] + nums[k]
        if current > 0:
            if j == k - 1:
                if i == j - 1:
                    break
                else:
                    i += 1
                    j = i + 1
                    k = j + 1
            else:
                j += 1
                k = j + 1
        else:
            if current == 0:
                result.append([nums[i], nums[j], nums[k]])
            if k == len(nums) - 1:
                if j == k - 1:
                    if i == j - 1:
                        break
                    else:
                        i += 1
                        j = i + 1
                        k = j + 1
                else:
                    j += 1
                    k = j + 1
            else:
                k += 1
    for i in result:
        if i not in result2:
            result2.append(i)
    return result2


def new(nums):
    if len(nums) < 3:
        return []
    result = []
    result2=[]
    nums.sort()
    for i in range(len(nums)-2):
        target = nums[i]
        j = i + 1
        k = len(nums) - 1
        for _ in range(len(nums) - i-1):
            value = nums[j] + nums[k]
            if value+target == 0:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif value+target > 0:
                k -= 1
            else:
                j += 1
            if j >= k:
                break
    for i in result:
        if i not in result2:
            result2.append(i)
    return result2


inp = []
inp2=[-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(new(inp2))
