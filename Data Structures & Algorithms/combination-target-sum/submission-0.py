class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = [] # hold temp result arrays

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            # break case, too big target or no more nums
            if i >= len(nums) or total > target:
                return
            
            # take nums[i] decision tree path
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # reject nums[i]
            # note the i+1 since now we move to next element
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res

        