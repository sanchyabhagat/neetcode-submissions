class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # pick i
            subset.append(nums[i])
            dfs(i+1)

            # undo
            subset.pop()

            # reject i till i and i+1 element is same
            while i + 1 < len(nums) and nums[i] == nums[i+1]: i += 1
            dfs(i+1)
        
        dfs(0)
        return res
        