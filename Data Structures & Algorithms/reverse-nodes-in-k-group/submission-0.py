# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        groupPrev = dummy
       
        while True:
            kth = self.getKth(groupPrev, k)
            # terminal condition, no more valid groups 
            if not kth:
                break
        
            # save the k.next first before reversing
            # this will starting point for next loop
            groupNext = kth.next

        #    reversing groups of size k
            # instead of last pointer to None, we can point it to the next group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
        
            # preprare for next group
            tmp = groupPrev.next # initially first node in our group
            # connect new reversed last to kth
            groupPrev.next = kth
            # new group prev 
            groupPrev = tmp
        return dummy.next



    def getKth(self, cur, k):
        # increment till we move k elements or hit end of list
        while cur and k > 0:
            cur = cur.next
            k -=1
        
        return cur
    