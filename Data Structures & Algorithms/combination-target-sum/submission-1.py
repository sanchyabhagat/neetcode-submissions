class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # cur -> temp holding area for a potential result
        def dfs(i, cur, total):
            # happy path
            if total == target:
                res.append(cur.copy())
                return
            
            # overshot
            if i >= len(nums) or total > target:
                return
            
            # pick i AND stay at i to reuse potentially 
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # dont pick i
            cur.pop()
            dfs(i+1, cur, total)

        
        dfs(0, [], 0)
        return res

        