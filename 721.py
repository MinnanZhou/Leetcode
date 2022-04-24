from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):
        notebook = defaultdict(list)
        for account in accounts:
            group = []
            newGroup = set(account[1:])
            for i, branch in enumerate(notebook[account[0]]):
                for a in account[1:]:
                    if a in branch:
                        group.append(i)
                        break
            for element in group[::-1]:
                newGroup = newGroup.union(notebook[account[0]].pop(element))
            notebook[account[0]].append(newGroup)
        ret = []
        for item in notebook.items():
            name = item[0]
            for p in item[1]:
                ret.append([name] + sorted(list(p)))
        return ret


a = Solution()
inp = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
print(a.accountsMerge(inp))
