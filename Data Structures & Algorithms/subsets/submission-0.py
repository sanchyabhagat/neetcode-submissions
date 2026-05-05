class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # hold final res
        res = []

        # hold current subset for each level of dfs
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # take i-th element
            subset.append(nums[i])
            dfs(i+1)

            # reject i-th element
            subset.pop()
            dfs(i+1)
        
        # main call to dfs to start the backtracking
        dfs(0)

        return res
        