class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        minHeap = [[0, k]]
        res = 0
        visit = set()

        adj = collections.defaultdict(list)

        for u,v,w in times:
            adj[u].append([v,w])


        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            # current result so far
            res = w1

            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [w1+w2, n2])
        
        return res if len(visit) == n else -1

        