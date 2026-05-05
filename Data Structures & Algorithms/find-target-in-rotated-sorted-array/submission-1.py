class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find rotation/pivot point - where left and right side are sorted
        l,r = 0, len(nums)-1
        # example: [4,5,6,1,2,3]
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            
            else:
                r = m
        # pivot point found, now search left and right of this with separate 
        # binary searches
        pivot = l

        def bin_search(left: int, right: int):
            while left <= right:
                m = (left+right) // 2
                
                if nums[m] == target:
                    return m
                
                elif nums[m] > target:
                    right = m - 1
                
                else:
                    left = m + 1
            return -1
        
        result = bin_search(0, pivot-1)
        if result != -1:
            return result
        
        return bin_search(pivot, len(nums)-1)
            

        
        


            

