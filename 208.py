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

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True if self.isword else False
        if word[0] in self.nodes:
            return self.nodes[word[0]].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        if prefix[0] in self.nodes:
            return self.nodes[prefix[0]].startsWith(prefix[1:])
        else:
            return False


# Your Trie object will be instantiated and called as such:
inp1 = ["Trie", "insert", "search", "search", "sear"]
inp2 = ["apple", "apple", "app", "app", "app", "app"]
obj = Trie()
for item in inp1:
    obj.insert(item)
    print(obj.search('sear'))
for item in inp2:
    print(obj.startsWith("sear"))
