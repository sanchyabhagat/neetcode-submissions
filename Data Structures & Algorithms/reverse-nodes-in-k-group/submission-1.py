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

            # terminal condition
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            
            # move groupPrev, etc to the next group
            
            # save curr prev
            tmp = groupPrev.next
            groupPrev.next = kth # connect this to the start

            groupPrev = tmp # move this to the new reversed end - ready at start of the next group
        
        return dummy.next

    def getKth(self, curr, k) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

            


        