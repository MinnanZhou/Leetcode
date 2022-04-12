class Solution:
    def findRestaurant(self, list1, list2):
        set1 = {list1[i]: i for i in range(len(list1))}
        res = float('inf')
        ret = []
        for index, test in enumerate(list2):
            if test in set1:
                if index + set1[test] == res:
                    ret.append(test)
                elif index + set1[test] < res:
                    ret = [test]
                    res = index + set1[test]
        return ret


a = Solution()
inp = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
inp2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(a.findRestaurant(inp, inp2))
