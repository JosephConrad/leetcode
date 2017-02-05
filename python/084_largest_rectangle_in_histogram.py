class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [0]
        r = 0
        for i in range(1, len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                r = max(r, w * h)
            stack.append(i)
        return r


if __name__ == "__main__":
    print Solution().largestRectangleArea([2, 1, 4, 5, 3, 4])
