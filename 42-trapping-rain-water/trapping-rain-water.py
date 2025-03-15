class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                dist = i - stack[-1] - 1
                ht = min(height[i], height[stack[-1]]) - height[top]
                res += (dist * ht)
            stack.append(i)
        return res