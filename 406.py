class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: [x[0], -x[1]])
        q = [[] for _ in range(len(people))]
        seat = [i for i in range(len(people))]
        for individual in people:
            q[seat[individual[1]]] = individual
            seat.remove(seat[individual[1]])
        return q


a = Solution()
inp = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print(a.reconstructQueue(inp))
