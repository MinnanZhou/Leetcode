def func(intervals):
    intervals.sort()
    ret=[intervals[0]]
    for i in intervals[1:]:
        if i[0]>ret[-1][1]:
            ret.append(i)
        else:
            ret[-1][1]=max(i[1],ret[-1][1])
    return ret

inp=[[1,3],[0,6],[8,10],[15,18]]
print(func(inp))