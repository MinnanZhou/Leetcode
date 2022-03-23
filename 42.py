class Solution:
    def trap(self, height) -> int:
        left = 0
        right = 1
        water = [0 for i in range(len(height))]
        result = 0
        while left != len(height):
            while True:
                if right >= len(height):
                    if left == len(height) - 1:
                        break
                    right = left + 1
                    height[left] -= 1
                    if height[left] <= height[right]:
                        break
                if height[left] > height[right]:
                    right += 1
                else:
                    water[left:right] = [height[left] for _ in range(right - left)]
                    left = right
                    right += 1
            left += 1
            right = left + 1
        for i in range(len(height)):
            result += max(0, water[i] - height[i])
        return result

    def findmax(self, height):
        maxpos = [0]
        maxvalue = max(height)
        for i in range(len(height)):
            if height[i] == maxvalue:
                maxpos.append(i)
        return maxpos

    def func(self, height):
        position = self.findmax(height)
        result = 0
        for i in range(len(position) - 1):
            result += self.trap(height[position[i]:position[i + 1] + 1])
        result += self.trap(height[position[-1] - len(height) - 2:-1])
        return result


a = Solution()
inp = [4, 2, 3]
print(a.trap(inp))
