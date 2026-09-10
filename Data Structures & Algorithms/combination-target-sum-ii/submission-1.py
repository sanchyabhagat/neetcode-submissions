class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort first to avoid duplicates
        # go through each posible cadidate starting at index 0
        # pass in index, current array, current sum
        # it curent sum matches target, keep a copy of the result
        # backtracking DFS - so pick and then remove from total and skip till the item si same

        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, cur, total):
            # base case
            if total == target:
                res.append(cur.copy())
                return
            
            # bad case - overshot
            if i == n or total > target:
                return
            
            # case 1 pick ith
            cur.append(candidates[i])

            dfs(i+1, cur, total + candidates[i])

            # reset
            cur.pop()
            while(i < n-1 and candidates[i] == candidates[i+1]): i += 1
            dfs(i+1, cur, total)

            return


        

        dfs(0, [], 0)

        return res
        
