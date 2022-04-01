class Solution:
    def circularArrayLoop(self, offset) -> bool:
        index_set = set([i for i in range(len(offset))])
        n = len(offset)
        while index_set:
            index = index_set.pop()
            slow, quick = index, index
            flag = 0
            while flag < 2 or slow != quick:
                if slow == quick: flag += 1
                slow = (slow + offset[slow]) % n
                quick = (quick + offset[quick]) % n
                quick = (quick + offset[quick]) % n
                if slow in index_set: index_set.remove(slow)
                if offset[slow] * offset[(slow + offset[slow]) % n] < 0:
                    flag = -1
                    break
            if flag >= 0 and abs(offset[slow]) % n != 0:
                return True
        return False


a = Solution()
inp = [1, 1, 1, 1, 1, 1, 1, 1, 1, -5]
print(a.circularArrayLoop(inp))
