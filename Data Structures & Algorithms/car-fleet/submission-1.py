class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for (p,s) in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for p,s in pairs:
            # time
            stack.append((target-p) / s)

            # check if valid car group, cur stack added time <= previous stack top time
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                # form group, remove the extra
                stack.pop()
        
        return len(stack)
        