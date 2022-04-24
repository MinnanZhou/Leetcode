class Codec:
    def __init__(self):
        self.table = [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        self.set = {self.table[i]: i for i in range(62)}
        self.memory = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        h = self.convert(hash(longUrl))
        self.memory[h] = longUrl
        return h

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.memory[shortUrl]

    def convert(self, s):
        ret = ''
        while s != -1 and s // 62:
            ret += self.table[s % 62]
            s = s // 62
        ret += self.table[s % 62]
        ret = ret[::-1]
        return ret


a = Codec()
x = a.encode("https://leetcode.com/problems/design-tinyurl")
y = a.decode(x)
print(y)
