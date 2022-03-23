class Solution:
    def containsDuplicate(self, nums) -> bool:
        subset = set()
        for num in nums:
            if num not in subset:
                subset.add(num)
            else:
                return True
        return False
