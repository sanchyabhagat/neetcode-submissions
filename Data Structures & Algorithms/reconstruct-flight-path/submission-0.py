class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. adj list
        # 2. dfs
        # 3. when no viable path - return False
        # 4. start enumerating neighbors
        # 5. Add neighbvor to res and resmove from adj list
        # 6: Return True if dfs now passes
        # 7. backtrack and remove current node from res and add it back to the adj list to backtrack
        # viable condition len(res) = len(tickets) + 1 (for JFK initial)

        tickets.sort()
        adj = {src: [] for src, dst in tickets}

        for u,v in tickets:
            adj[u].append(v)

        res = []
        res.append("JFK")

        def dfs(n):
            # main true condition
            if len(res) == len(tickets) + 1:
                return True
            
            if n not in adj: return False

            # copy since we will modify our original list
            temp = list(adj[n])
            for i, nei in enumerate(temp):
                adj[n].pop(i)
                res.append(nei)

                if dfs(nei): return True

                # reset as if neighbor failed to find valid path, add back at same index
                adj[n].insert(i, nei)
                res.pop()
            
            return False
        
        dfs("JFK")
        return res





            
        
        