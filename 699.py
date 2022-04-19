import bisect


class Solution:
    def fallingSquares(self, positions):
        height = {0: 0}
        ret = [0]
        for point, h in positions:
            keypoint = sorted(list(height.keys()))

            p_l = bisect.bisect_right(keypoint, point)
            p_r = bisect.bisect_left(keypoint, point + h)
            base = max(height[k] for k in keypoint[p_l-1:p_r])

            new_height = base + h
            height[point] = new_height
            height[point + h] = height[keypoint[p_r-1]]
            for pos in keypoint[p_l:p_r]:
                height.pop(pos)
            ret.append(max(ret[-1], new_height))
        return ret[1:]


a = Solution()
inp=[[9,7],[1,9],[3,1]]
print(a.fallingSquares(inp))
