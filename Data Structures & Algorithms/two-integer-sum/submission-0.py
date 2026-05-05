class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hashmap to check if target-curElement exists at eeverypoint
        # if not - add current element to hasmap with it's index as value
        # guaranteed to find soln

        indexMap = {}

        for i,n in enumerate(nums):
            if target-n in indexMap:
                # smaller index first
                return [indexMap.get(target-n), i]
            
            indexMap[nums[i]] = i
        
        