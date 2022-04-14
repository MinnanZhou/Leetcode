class Trie:

    def __init__(self):
        self.nodes = {}
        self.isword = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.isword = True
            return
        if word[0] not in self.nodes:
            self.nodes[word[0]] = Trie()
        self.nodes[word[0]].insert(word[1:])

    def findRoot(self, word: str, i) -> str:
        if i >= len(word) or word[i] not in self.nodes:
            return word
        elif self.nodes[word[i]].isword:
            return word[:i + 1]
        else:
            return self.nodes[word[i]].findRoot(word, i + 1)


class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        Tree=Trie()
        for d in dictionary:
            Tree.insert(d)
        ret = ''
        for word in sentence.split(' '):
            ret += (Tree.findRoot(word, 0) + ' ')
        return ret[:-1]


a = Solution()
print(a.replaceWords(dictionary=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery"))
