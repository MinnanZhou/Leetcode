class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(int('0b' + a, 2) + int('0b' + b, 2))
