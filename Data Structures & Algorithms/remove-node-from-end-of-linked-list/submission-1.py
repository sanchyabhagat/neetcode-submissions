# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy starts at one step before start to make sure we reach ONE before delete
        # Idea is to have a fast and slow pointer with differnec of "n"
        # when fast reaches the end of list, slow will be at the target element
        # assuming we start ONE before - very important

        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        # get fast to n elements ahead
        while n > 0:
            fast = fast.next
            n -= 1
        
        # now start moving both
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Edge case if slow is at the end somehow
        if slow.next == None:
            return None
        
        # else remove from list,
        # now we are one behind target deletion
        slow.next = slow.next.next

        # original head tracker
        return dummy.next

        