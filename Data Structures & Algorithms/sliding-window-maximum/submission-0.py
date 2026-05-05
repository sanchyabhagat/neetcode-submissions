class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonically decreasing Queue
        # we want to add and remove element from beginning in O(1)
        # Why no stack? When window shifts, we want to be able to remove element from the left side
        # i.e. popLeft() when moving window to right
        # maxValue will be leftmost value in deque
        # when adding new element 
        # also popright() till new element to be added > rightmost value in deque

        
        q = collections.deque() # store indices
        l = r = 0
        res = []

        while r < len(nums):
            # add right element 
            #and pop till it is greater than the smallest element in the deque
            while q and nums[q[-1]] < nums[r]:
                q.pop() # pop right element
            q.append(r)

            # remove left element if leftmost element of queue has moved up
            if l > q[0]:
                q.popleft()
            
            # result case - when we have a valid window size add to queue
            # max element will be the leftmost element in deque since it is in decreasing order
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            
            # always move r
            r += 1
        
        return res
            






