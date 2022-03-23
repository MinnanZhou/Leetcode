def func(candidates, target):
    candidates.sort()
    ret = []
    result = []
    combine(candidates, target, [], ret)
    for i in ret:
        if i not in result:
            result.append(i)
    return result


def combine(candidates, target, path, result):
    if target < 0:
        return
    if target == 0:
        result.append(path)
        return
    for i in range(len(candidates)):
        if i > 0 and candidates[i] == candidates[i - 1]:
            continue
        combine(candidates[i + 1:], target - candidates[i], path + [candidates[i]], result)


inp = [10,1,2,7,6,1,5]
val = 8
print(func(inp, val))
