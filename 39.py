def func(candidates, target):
    ret = []
    combine(candidates, target, [], ret)
    return ret


def combine(candidates, target, path, result):
    if target < 0:
        return
    if target == 0:
        result.append(path)
        return
    for i in range(len(candidates)):
        combine(candidates[:i+1], target - candidates[i], path + [candidates[i]], result)


inp = [2, 3, 7]
val = 7
print(func(inp, val))
