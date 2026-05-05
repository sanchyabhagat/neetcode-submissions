class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        length = len(heights)

        for i,h in enumerate(heights):
            startIndex = i # determine the new starting index for next element we add to the stack to maximize possible rectangle area
            while stack and stack[-1][1] > h:
                popIndex, popHeight = stack.pop()
                maxArea = max(maxArea, popHeight * (i - popIndex))
                startIndex = popIndex # move the start index to maximize area
            stack.append((startIndex, h))
        
        ## Handle pending stack elements
        for i,h in stack:
            maxArea = max(maxArea, h * (length - i))
        return maxArea
        