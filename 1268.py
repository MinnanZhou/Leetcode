import bisect


class Solution:
    def suggestedProducts(self, products, searchWord: str):
        products.sort()
        ret = []
        left, right = 0, len(products)
        for i in range(len(searchWord)):
            left = bisect.bisect_left(products[left:right], searchWord[:i + 1]) + left
            right = bisect.bisect_left(products[left:right], searchWord[:i] + chr(ord(searchWord[i]) + 1)) + left
            ret.append(products[left:min(right, left + 3)])
        return ret


a = Solution()
inp = ["code","codephone","coddle","coddles","codes"]
inp2 = "coddle"
print(a.suggestedProducts(inp, inp2))
