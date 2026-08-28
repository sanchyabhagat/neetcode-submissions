class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # adj list
        adj = collections.defaultdict(list)
        
        # weight, signl name
        minHeap = [(0, k)]

        res = 0
        visit = set()

        for u,v,w in times:
            adj[u].append((v, w))

        while minHeap:
            w1, v1 = heapq.heappop(minHeap)

            if v1 in visit:
                continue
            
            visit.add(v1)
            # set res to current min weight
            res = w1

            # add neighbors
            for v2, w2 in adj[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (w2+w1, v2))
            
        
        return res if len(visit) == n else -1

            

        