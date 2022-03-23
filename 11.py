def maxArea(height) -> int:
    total = len(height)
    j = total - 1
    i = 0
    de = 0
    water = []
    for _ in range(total):
        if i >= j:
            break
        else:
            if de == 0:
                water.append((j - i) * min(height[i], height[j]))
            if height[i] > height[j]:
                if height[j] >= height[j - 1]:
                    de = 1
                else:
                    de = 0
                j -= 1
            else:
                if height[i] >= height[i + 1]:
                    de = 1
                else:
                    de = 0
                i += 1
    return max(water)


inp = [1, 18, 6, 2, 15,18, 4, 8, 3, 7]
print(maxArea(inp))
