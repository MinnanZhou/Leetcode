from collections import defaultdict


class Trie:

    def __init__(self):
        self.nodes = {}
        self.index = -1

    def insert(self, word: str, i) -> None:
        if len(word) == 0:
            self.index = i
            return
        if word[0] not in self.nodes:
            self.nodes[word[0]] = Trie()
        self.nodes[word[0]].index = i
        self.nodes[word[0]].insert(word[1:], i)

    def startsWith(self, prefix: str) -> int:
        if len(prefix) == 0:
            return self.index
        if prefix[0] in self.nodes:
            # if len(prefix) == 1:
            #     return max([k.index for k in self.nodes.values()])
            return self.nodes[prefix[0]].startsWith(prefix[1:])
        else:
            return -1


# class WordFilter:
#
#     def __init__(self, words):
#         self.tree = Trie()
#         for i, v in enumerate(words):
#             long = v + '#' + v
#             for j in range(len(v)):
#                 self.tree.insert(long[j:], i)
#
#     def f(self, prefix: str, suffix: str) -> int:
#         return self.tree.startsWith(suffix + '#' + prefix)

class WordFilter:

    def __init__(self, words):
        self.prefix = defaultdict(set)
        self.suffix = defaultdict(set)
        for i, w in enumerate(words):
            for j in range(len(w)):
                self.prefix[w[:j + 1]].add(i)
                self.suffix[w[j:]].add(i)

    def f(self, pref: str, suff: str) -> int:
        res = list(self.prefix[pref].intersection(self.suffix[suff]))
        return max(res) if res else -1


a = WordFilter(
    ["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa", "accabaccaa", "cabcbbbcca", "ababccabcb",
     "caccbbcbab", "bccbacbcba"])
b = [["bccbacbcba", "a"], ["ab", "abcaccbcaa"], ["a", "aa"], ["cabaaba", "abaaaa"], ["cacc", "accbbcbab"],
     ["ccbcab", "bac"], ["bac", "cba"], ["ac", "accabaccaa"], ["bcbb", "aa"], ["ccbca", "cbcababac"]]
for inp in b:
    print(a.f(inp[0], inp[1]))
