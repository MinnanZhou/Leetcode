class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = set([2 ** i for i in range(32)])
        return n in result
        # if n==1:
        #     return True
        # elif n>0 and n%2==0:
        #     return self.isPowerOfTwo(n//2)
        # return False

a = Solution()
print(a.isPowerOfTwo(123))
