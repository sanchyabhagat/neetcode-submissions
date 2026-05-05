class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Algorithm
        # 1. Find smaller arra, assign it A, call the bigger B
        # 2. l, r = 0 , len(A) - 1 for bin search on A
        # While true, find mid point of A -> i
        # Find Aleft = A[i] or float("-infinity"), ARight, BLeft, BRight
        # Condition for success: ALeft <= BRight and Bleft <= ARight
        # Success -> odd total -> return the single mid -> min(Aright, Bright)
        # Success -> even total -> return max (lefts) + min (rights) / 2 (decimal)
        # Else Aleft > BRight -> get less from A -> r = m-1
        # else Bleft > Aright -> get more from A -> l = m +1

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 # floor

        if (len(B) < len(A)):
            A , B = B , A # swap, make A smaller
        
        l, r = 0, len(A)-1
        while True:
            
            i = (l+r) // 2
            # offset by 2 to account for 0 starting point for i and j
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity") # account for out of bound son left
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity") # account for out of bound son left
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            # success
            if (Aleft <= Bright and Bleft <= Aright ):
                # odd
                if total % 2 == 1:
                    return min(Aright, Bright)
                
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2

            # A has invalid larger elements
            elif (Aleft > Bright):
                r = i - 1
            # Get more from A, smaller elements
            else:
                l = i + 1
        