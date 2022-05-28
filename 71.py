class Solution:
    def simplifyPath(self, path: str) -> str:
        visited = []
        i, j = 0, 0
        folder = ''
        path += '/'
        while i < len(path):
            if path[i] == '/':
                if len(folder) > 0:
                    visited.append(folder)
                    folder = ''
            else:
                folder += path[i]
            i += 1
        res = '/'
        while j < len(visited):
            if visited[j] == '.':
                visited.pop(j)
            elif visited[j] == '..':
                visited.pop(j)
                if j > 0:
                    visited.pop(j - 1)
                    j -= 1
            else:
                j += 1
        res += '/'.join(visited)
        return res


a = Solution()
inp = "/home/../../.."
print(a.simplifyPath(inp))
