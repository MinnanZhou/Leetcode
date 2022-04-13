from functools import cache


class Solution:
    def shoppingOffers(self, price, special, needs) -> int:
        realSpecial = []
        for package in special:
            if sum(package[p] * price[p] for p in range(len(price))) > package[-1]:
                realSpecial.append(package)

        @cache
        def dp(i, remain):
            total = 0
            if i > len(realSpecial) - 1:
                return sum([price[k] * remain[k] for k in range(len(remain))])
            if all([realSpecial[i][j] <= remain[j] for j in range(len(remain))]):
                ch1 = dp(i + 1, tuple([remain[k] - realSpecial[i][k] for k in range(len(remain))]))
                ch2 = dp(i, tuple([remain[k] - realSpecial[i][k] for k in range(len(remain))]))
                ch3 = dp(i + 1, remain)
                total += min(ch1 + realSpecial[i][-1], ch2 + realSpecial[i][-1], ch3)
            else:
                ch3 = dp(i + 1, remain)
                ch4 = sum([price[k] * remain[k] for k in range(len(remain))])
                return min(ch3, ch4)
            return total

        ret = dp(0, tuple(needs))
        return ret


a = Solution()
print(a.shoppingOffers(price=[6, 3, 6, 9, 4, 7], special=[[1, 2, 5, 3, 0, 4, 29], [3, 1, 3, 0, 2, 2, 19]],
                       needs=[4, 1, 5, 2, 2, 4]))
