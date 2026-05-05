class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-ford algo
        # similar to BFS - O(E.V) but for this O(E.k)
        # Hard to use djikstras with weighted edges since we are AT MOST k stops not exact k stops

        # setup prices to be inf to mark them unreachable by default
        prices = [float("inf")] * n

        # price of src is zero to start
        prices[src] = 0

        # loop k+1 times, 1 extra to represent direct flights in cae k=0
        for i in range(k+1):
            # tmp prices so as to not mutate current layer too early
            tmpPrice = prices.copy()

            for s, d , p in flights:
                # check if src was unreachable
                if prices[s] == float("inf"):
                    continue
                
                # check if lower price available at this layer only
                # checking  tmpPrice[d] in case a lower price was already found at this layer
                if prices[s] + p < tmpPrice[d]:
                    tmpPrice[d] = prices[s] + p
            
            prices = tmpPrice
        
        return -1 if prices[dst] == float("inf") else prices[dst]




