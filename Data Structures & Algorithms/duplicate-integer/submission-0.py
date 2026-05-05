class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visit = set()

        for n in nums:
            if n in visit:
                return True
            
            visit.add(n)
        
        return False
        