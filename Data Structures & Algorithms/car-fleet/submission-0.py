class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for (p,s) in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        # Reverse sorted
        for p,s in pairs:
            # time = distance / speed
            stack.append((target-p)/s)
            # pop stack element means we are combining cars into a single car fleet
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)
        