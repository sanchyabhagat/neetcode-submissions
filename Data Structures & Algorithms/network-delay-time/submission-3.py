class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dict to store adj list with weights
        # minHeap store (weight, vertice) to track minimum distances
        # each time we visit, we add to visit set
        # add each edges with current weight and weight to reach the edge
        # at the end we eitehr visited all or failed to based
        # on len(visit)

        adj = collections.defaultdict(list)
        visit = set()

        # weight for starting elemnt is always zero
        minHeap = [(0 , k)]
        res = 0

        for u,v,w in times:
            adj[u].append((v, w))
        
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)

            # base case
            if v1 in visit:
                continue
                
            visit.add(v1)

            # current result min at this point
            res = w1

            for v2, w2 in adj[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, v2))
        
        return res if len(visit) == n else -1

            
        