class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def doOperation(a, b, t) -> int:
            if t == "+":
                return a+b
            
            elif t == "-":
                return a-b
            
            elif t == "*":
                return a*b
            
            elif t == "/":
                return int(a/b)
        
        stack = []
        op = ["+", "-", "*", "/"]
        for t in tokens:
            if t in op:
                b = int(stack.pop())
                a = int(stack.pop())
                res = doOperation(a, b, t)
                stack.append(res)
            else:
                stack.append(t)
        return int(stack[-1])
        
            