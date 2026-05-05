class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Global
        stack = []
        result = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
            
            # open condition - open < n
            if (openN < n):
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            # close condition - closeN < openN
            if (closeN < openN):
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0,0)
        return result

        