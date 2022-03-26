class Solution:

    def isRectangleCover(self, rectangles) -> bool:
        corners = {0: set(), 1: set(), 2: set(), 3: set()}
        for rectangle in rectangles:
            c = [(rectangle[0], rectangle[1]), (rectangle[2], rectangle[1]),
                 (rectangle[0], rectangle[3]), (rectangle[2], rectangle[3])]
            for index, corner in enumerate(c):
                state = 0
                for i in range(4):
                    if corner in corners[i]:
                        state = 1
                        if i == index:
                            return False
                        elif i == 3 - index:
                            corners[index].add(corner)
                            break
                        else:
                            corners[i].remove(corner)
                            break
                if not state:
                    corners[index].add(corner)
        return True if sum([len(corners[i]) for i in range(4)]) == 4 else False


a = Solution()
inp = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
print(a.isRectangleCover(inp))
