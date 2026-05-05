# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # start from the left of first elemen,
        # ensures we reach one step before the element to delete
        dummy = ListNode(0, head)
        second = dummy
        # start at first element 
        first = head

        while n > 0:
            first = first.next
            n -= 1
        
        while first:
            first = first.next
            second = second.next
        
        if second.next == None:
            return None
        
        second.next = second.next.next

        return dummy.next
        

        