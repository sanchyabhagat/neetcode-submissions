class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # negative since we're doing min heap, min negative == max positive
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x - y) # x-y since we want negative number inserted
            
        # base case of 0 in case of empty stones
        stones.append(0)
        
        return abs(stones[0])
            

        