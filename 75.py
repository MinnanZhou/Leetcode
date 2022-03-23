class Solution:
    def sortColors(self, nums) -> None:
        zeros=0
        twos=0
        i=0
        while i<len(nums)-twos:
            if nums[i]==0:
                nums[i], nums[zeros]=nums[zeros],nums[i]
                zeros+=1
                i+=1
            elif nums[i]==2:
                nums[i], nums[-1-twos] = nums[-1-twos], nums[i]
                twos+=1
            else:
                i+=1


a=Solution()
inp=[2,0,2,1,1,0]
a.sortColors(inp)