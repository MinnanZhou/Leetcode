class Solution:
    def asteroidCollision(self, asteroids):
        stones = []
        ret = []
        for ast in asteroids:
            if ast < 0:
                if not stones:
                    ret.append(ast)
                else:
                    while stones[-1] <= abs(ast):
                        if stones[-1] == abs(ast):
                            stones.pop()
                            break
                        else:
                            stones.pop()
                            if not stones:
                                ret.append(ast)
                                break
            else:
                stones.append(ast)

        return ret + stones


a = Solution()
inp = [-3, 10, 2, -5, 8, -10]
print(a.asteroidCollision(inp))
