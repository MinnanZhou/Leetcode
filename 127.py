class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        used = {beginWord}
        current = [beginWord]
        later = []
        n = len(wordList)
        steps = 1
        wordSet = set(wordList)

        while len(used) < n + 2 and current:
            while current:
                start = current.pop()
                if start == endWord:
                    return steps
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(start)):
                        x = start[:i] + letter + start[i + 1:]
                        if x in wordSet and x not in used:
                            later.append(x)
                            used.add(x)

            current = later.copy()
            later.clear()
            steps += 1

        return 0


a = Solution()
inp = 'hit'
inp2 = 'cog'
inp3 = ["hot", "dot", "dog", "lot", "log", "cog"]
print(a.ladderLength(inp, inp2, inp3))
