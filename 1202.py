class Solution:
    def __init__(self):
        self.parent = []

    def union(self, p1, p2):
        self.parent[self.find(p1)] = self.find(p2)

    def find(self, p1):
        if self.parent[p1] != p1:
            self.parent[p1] = self.find(self.parent[p1])

        return self.parent[p1]

    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        self.parent = list(range(len(s)))
        res = list(s)
        for a, b in pairs:
            self.union(a, b)

        groups = {}
        for i in range(len(s)):
            ance = self.find(i)
            if ance not in groups:
                groups[ance] = [i]
            else:
                groups[ance].append(i)

        for group in groups.values():
            s_new = sorted(s[x] for x in group)
            group.sort()
            for i in range(len(s_new)):
                res[group[i]] = s_new[i]

        return ''.join(res)


a = Solution()
inp = 'sdfsdfuklwef'
inp2 = [[1, 0], [7, 1], [9, 1], [3, 0], [7, 1], [0, 4], [6, 5], [2, 6], [6, 4], [6, 0]]
print(a.smallestStringWithSwaps(inp, inp2))
