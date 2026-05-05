class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm, pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
        
            # add possible perms without duplicates
            for i in range(len(nums)):
                # if current ith element is not in current perm
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(perm,pick)
                    # reset back as if we never added current nums[i]
                    perm.pop()
                    pick[i] = False
        
        dfs([], [False] * len(nums))
        return res        

        