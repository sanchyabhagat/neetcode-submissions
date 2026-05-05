# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # whybdoes this work: Floyd's Tortoise and hare
        # atmost the distance between fast and slow will be n-1
        # and each iteration the distance gets reduced by 1 (+2 - 1)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
        