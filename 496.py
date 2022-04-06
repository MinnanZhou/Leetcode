class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack_set = {nums2[-1]: -1}
        stack = [-1]
        for i in range(len(nums2) - 2, -1, -1):
            if nums2[i] == nums2[i + 1]:
                stack_set[nums2[i]] = stack_set[nums2[i + 1]]
                stack.append(stack_set[nums2[i + 1]])
            elif nums2[i] < nums2[i + 1]:
                stack_set[nums2[i]] = nums2[i + 1]
                stack.append(nums2[i + 1])
            else:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                stack_set[nums2[i]] = stack[-1] if stack else -1
                stack.append(stack[-1] if stack else -1)
        return [stack_set[num1] for num1 in nums1]


a = Solution()
inp = [2, 4]
inp2 = [1,2, 6, 4, 3, 5]
print(a.nextGreaterElement(inp, inp2))
