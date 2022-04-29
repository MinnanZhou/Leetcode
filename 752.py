from collections import deque


class Solution:
    def openLock(self, deadends, target: str) -> int:
        t = int(target)
        target = [0, 0, 0, 0]
        visited = set()
        for i in range(4):
            target[3 - i] = t % 10
            t = t // 10
        target = tuple(target)
        for d in deadends:
            int_d = int(d)
            list_d = [0, 0, 0, 0]
            for i in range(4):
                list_d[3 - i] = int_d % 10
                int_d = int_d // 10
            visited.add(tuple(list_d))
        q = deque([(0, 0, 0, 0)])
        steps = 0
        next_gen = []
        while q:
            position = q.popleft()
            if position == target: return steps
            if position not in visited:
                base = list(position)
                for i in range(4):
                    p0 = tuple(base[:i] + [(base[i] + 1) % 10] + base[i + 1:])
                    p1 = tuple(base[:i] + [(base[i] - 1) % 10] + base[i + 1:])
                    if p0 not in visited: next_gen.append(p0)
                    if p1 not in visited: next_gen.append(p1)
            visited.add(position)
            if not q:
                q += next_gen
                next_gen = []
                steps += 1
        return -1


a = Solution()
inp = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
inp2 = "8888"
print(a.openLock(inp, inp2))
