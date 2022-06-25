from functools import lru_cache


class Trie:
    def __init__(self):
        self.isWord = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.tree = Trie()

    def addWord(self, word: str) -> None:
        if not self.search(word):
            self.search.cache_clear()
            node = self.tree
            for l in word:
                node = node.children.setdefault(l, Trie())
            node.isWord = True

    @lru_cache
    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i >= len(word):
                return node.isWord
            if word[i] in node.children:
                return dfs(i + 1, node.children[word[i]])
            if word[i] == '.':
                for n in node.children.values():
                    if dfs(i + 1, n): return True
            return False

        return dfs(0, self.tree)


a = WordDictionary()
a.addWord('badas')
a.addWord('bad')
print(a.search('...'))
