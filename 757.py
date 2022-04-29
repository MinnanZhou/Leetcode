class Solution:
    def intersectionSizeTwo(self, intervals) -> int:
        intervals.sort(key=lambda x:(x[1],-x[0]))
        temp = []
        count = 0
        for left, right in intervals:
            if not temp or left > temp[1]:
                count += 2
                temp = [right - 1, right]
            elif left > temp[0]:
                count += 1
                temp = [temp[1], right]
        return count

a = Solution()
inp = [[1,3],[3,7],[5,7],[7,8]]
print(a.intersectionSizeTwo(inp))
