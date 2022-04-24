class Trie:
    def __init__(self):
        self.nodes = {}
        self.isword = set()

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return
        if len(word) == 1:
            self.isword.add(word)
        if word[0] not in self.nodes:
            self.nodes[word[0]] = Trie()
        self.nodes[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 1:
            return word in self.isword
        if word[0] in self.nodes:
            if word[0] not in self.isword: return False
            return self.nodes[word[0]].search(word[1:])
        else:
            return False


class Solution:
    def longestWord(self, words) -> str:
        root = Trie()
        ret = ''
        for word in words:
            root.insert(word)
        for word in words:
            if root.search(word):
                if len(word) > len(ret) or (len(word) == len(ret) and word < ret):
                    ret = word
        return ret


a=Solution()
inp=["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
print(a.longestWord(inp))