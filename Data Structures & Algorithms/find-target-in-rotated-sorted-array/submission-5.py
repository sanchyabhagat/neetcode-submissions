class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find rotation/pivot point - where left and right side are sorted
        l,r = 0, len(nums)-1
        # example: [4,5,6,1,2,3]
        
        while l <= r:
            m = (l + r) // 2
            if(nums[m] == target):
                return m

            # left sorted portion
            if(nums[l] <= nums[m]):
                # we are outside of bounds for left sorted, go to right
                if(target > nums[m] or target < nums[l]):
                    l = m + 1
                # we are in bound for left:
                else:
                    r = m - 1
            
            # right sorted portion:
            else:
                # we are out of bounds of right sorted portion, go to left
                if (target > nums[r] or target < nums[m]):
                    r = m - 1
                # we are good to search right bounds
                else:
                    l = m + 1
        
        return -1
            

        
        


            

