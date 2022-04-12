class Solution:
    def findDuplicate(self, paths):
        file_set = {}
        for p in paths:
            current_files = p.split(' ')
            root = current_files[0]
            current_files = current_files[1:]
            for file in current_files:
                filename = file.split('(')[0]
                content = file.replace(filename, '')[1:-1]
                if content in file_set:
                    file_set[content].append(root + '/' + filename)
                else:
                    file_set[content] = [root + '/' + filename]
        return [file_set[i] for i in file_set if len(file_set[i]) > 1]


a = Solution()
inp = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print(a.findDuplicate(inp))
