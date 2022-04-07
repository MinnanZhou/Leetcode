import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        hp = []
        program = sorted([[-i[1], i[0]] for i in zip(capital, profits)], key=lambda x: [-x[1]])
        while k > 0:
            while program and program[-1][1] <= w:
                heapq.heappush(hp, program.pop())
            if len(hp) == 0:
                return w
            w += -heapq.heappop(hp)[0]
            k -= 1
        return w


a = Solution()
inp = [1, 2, 3, 3, 2, 5, 1, 3, 5, 2, 5, 3, 6, 2, 6, 2, 9]
inp2 = [0, 1, 2, 8, 7, 9, 6, 4, 6, 3, 4, 5, 9, 2, 1, 9, 5]
print(a.findMaximizedCapital(3, 0, inp, inp2))
