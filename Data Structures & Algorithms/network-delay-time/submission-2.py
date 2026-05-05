class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #O ( E Log (v^2)) total edges == vertices ^ 2 approx
        edges = collections.defaultdict(list)
        
        for u,v,w in times:
            edges[u].append((v, w))
        
        # Add first initial vertices we start at with 0 weight
        minHeap = [(0, k)]
        visit = set()
        #  value for last node we will visit
        res = 0

        # execute till we have not reached all nodes
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)

            if v1 in visit:
                continue
            
            visit.add(v1)
            # Update result based on current distance
            res = w1

            # neighbors check
            for v2, w2 in edges[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, v2))
        
        return res if len(visit) == n else -1
