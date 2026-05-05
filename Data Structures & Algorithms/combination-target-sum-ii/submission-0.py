class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Important since we cant have duplicate results
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            # pick ith element
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()

            # dont pick ith but also skip till we have teh same value
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: i += 1

            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res

        