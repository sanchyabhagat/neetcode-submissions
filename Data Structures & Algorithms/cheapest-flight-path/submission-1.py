class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ## Runtime: O(k . E)
        prices = [float("inf")] * n
        # source point is zero cost rest is infinite for now
        prices[src] = 0

        # loop one for stops
        # k+1 because we need case with NO STOPS = 0
        for i in range(k+1):
            # copy prices so we dont edit in place
            # this is critical to respect num of stops
            tempPrices = prices.copy()

            # now for every edge
            for s,d,p in flights:

                # check if current source is unreachable
                # edge case
                if prices[s] == float("inf"):
                    continue
                
                # else we check if a lower price if available for destination d
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p
            
            # update prices
            prices = tempPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]

        