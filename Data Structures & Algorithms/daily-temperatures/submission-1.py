class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, tmp in enumerate(temperatures):
            while stack and stack[-1][1] < tmp:
                index, ele = stack.pop()
                res[index] = i - index
            
            stack.append([i, tmp])
        
        return res

        