class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        convert = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        def get(string):
            n = 0
            digit = 0
            for s in string[::-1]:
                n += convert[s] * 10 ** digit
                digit += 1
            return n

        return str(get(num1) * get(num2))
