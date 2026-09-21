class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            
            l = i+1
            r = len(nums)-1

            while l < r:
                ans = a + nums[l] + nums[r]

                if ans > 0:
                    r -= 1
                
                elif ans < 0:
                    l += 1
                
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l-1] == nums[l]:
                        l += 1
            
        return res
                    
        