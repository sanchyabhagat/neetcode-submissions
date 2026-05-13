class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        length = len(heights)

        for i,h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h:
                popi, poph = stack.pop()
                maxArea = max(maxArea, poph * (i - popi))
                startIndex = popi
            stack.append([startIndex, h])

        # rest of stack
        for i,h in stack:
            maxArea = max(maxArea, (length-i)*h)

        return maxArea 
        