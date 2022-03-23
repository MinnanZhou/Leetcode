class Solution:
    def insert(self,intervals, newItem):
        intervals.append(newItem)
        intervals.sort()
        ret=[intervals[0]]
        if len(intervals)==1:
            return ret
        for i in intervals[1:]:
            if i[0]>ret[-1][1]:
                ret.append(i)
                continue
            else:
                ret[-1][1]=max(ret[-1][1],i[1])
        return ret


a = Solution()
print(a.insert([[1,3],[6,9]], [2,5]))
