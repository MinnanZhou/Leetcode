class Solution:
    def validUtf8(self, data) -> bool:
        count = 0
        for num in data:
            if count == 0:
                if num < 128:
                    continue
                elif num > 191:
                    num_bin = bin(num)[2:]
                    for bit in num_bin:
                        if bit == '1':
                            count += 1
                        else:
                            break
                    count -= 1
                    if count >= 4:
                        return False
                else:
                    return False
            else:
                if 128 <= num <= 191:
                    count -= 1
                else:
                    return False
        return True if count == 0 else False


a=Solution()
inp=[250,145,145,145,145]
print(a.validUtf8(inp))