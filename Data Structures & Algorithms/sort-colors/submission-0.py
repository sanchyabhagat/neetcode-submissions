class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Three popinter - l, i, r
        # l -> all to left should be 0
        # r -> all to right be 2
        # i roaming incrementing to find possible swaps and IGNORE 1s
        # Dutch National Flag algorightm
        # !! VERY IMP ~!!!!!
        # WE DONOT increment i on right swap, since possible we could
        # have moved a 0 at the ith place which needs to be picked up by i
        l, r = 0, len(nums)-1
        i = 0

        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            
            elif nums[i] == 2:
                swap(i, r)
                # offset i by one, since we want to keep i the same for right swaps
                r -= 1
                i -= 1
            
            # incase of '1' continue 
            i += 1



        