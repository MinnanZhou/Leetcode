class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        letter = 'abcdefghijklmnopqrstuvwxyz'
        morse_set = {letter[i]: morse[i] for i in range(26)}
        word_set = set()
        for word in words:
            addone = ''
            for l in word:
                addone += morse_set[l]
            word_set.add(addone)
        return len(word_set)


a=Solution()
inp=["gin","zen","gig","msg"]
print(a.uniqueMorseRepresentations(inp))